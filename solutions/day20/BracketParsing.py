from typing import List

from solutions.utils.utils import Location


class Section:
    def follow_commands(self, locations: List[Location], map_layout) -> List[Location]:
        raise Exception(""
                        "Child classes of Section must implement: follow_commands(List[Location], Map)")


class StraightSection(Section):
    def __init__(self, content: str):
        if content.find("(") != -1:
            raise Exception(content + ": is not a straight section")
        self.__content = content

    def follow_commands(self, locations: List[Location], map_layout) -> List[Location]:
        return map_layout.follow_basic_command_lists(self.__content, locations)

    def __eq__(self, other: 'Section') -> bool:
        return (
                isinstance(other, StraightSection)
                and
                self.__content == other.__content
        )

    def __repr__(self):
        return self.__content


class BranchedSection(Section):
    def __init__(self, before_branch: Section, branches: List[Section], after_branch: Section):
        self.__before_branch = before_branch
        self.__branches = branches
        self.__after_branch = after_branch

    def follow_commands(self, locations: List[Location], map_layout) -> List[Location]:
        locations_before_branch = self.__before_branch.follow_commands(locations, map_layout)
        locations_after_branch = []
        for branch in self.__branches:
            locations_after_branch.extend(branch.follow_commands(locations_before_branch, map_layout))

        return self.__after_branch.follow_commands(locations_after_branch, map_layout)

    def __eq__(self, other: Section) -> bool:
        return (
                isinstance(other, BranchedSection)
                and
                self.__before_branch == other.__before_branch
                and
                self.__branches == other.__branches
                and
                self.__after_branch == other.__after_branch
        )

    def __repr__(self) -> str:
        return (
                str(self.__before_branch)
                + '(' +
                "|".join([str(branch) for branch in self.__branches])
                + ')' +
                str(self.__after_branch)
        )


class Commands:
    def __init__(self, commands: str):
        self.__commands = commands
        self.__cursor = 1

    def __current(self) -> str:
        return self.__commands[self.__cursor:]

    def __next_bracket(self) -> str:
        current = self.__current()
        next_open = current.find("(")
        next_pipe = current.find("|")
        next_close = current.find(")")
        if next_open == -1 and next_pipe == -1 and next_close == -1:
            return "$"
        if next_open != -1 and next_open < next_pipe and next_open < next_close:
            return "("
        if next_pipe != -1 and next_pipe < next_close:
            return "|"
        return ")"

    def __guard(self, type: str):
        if self.__next_bracket() == type:
            raise Exception(
                "Impossible control found: " + type
                + "; cursor at: " + str(self.__cursor)
                + "; neighbouring commands where: " + self.__commands[self.__cursor-5:self.__cursor+5]
            )

    def __next_bracket_position(self) -> int:
        return self.__current().find(self.__next_bracket())

    def __get_next_straight_section(self) -> StraightSection:
        return StraightSection(self.__current()[:self.__next_bracket_position()])

    def __move_till_after_next_bracket(self):
        self.__cursor += self.__next_bracket_position() + 1

    def parse(self) -> Section:
        return self.__parse(self.__get_next_straight_section())

    def __parse(self, already_parsed_before_section: Section) -> Section:

        # no brackets
        if self.__next_bracket() != "(":
            return already_parsed_before_section

        # before branch
        before_branch = already_parsed_before_section
        self.__move_till_after_next_bracket()

        branches = []
        current_section = self.__get_next_straight_section()
        self.__guard(")")

        do_while = True
        while do_while:
            if self.__next_bracket() == "|":
                branches.append(current_section)
                self.__move_till_after_next_bracket()
                current_section = self.__get_next_straight_section()

                # after_branch, branch_2 = self.parse_next_branch()
            elif self.__next_bracket() == "(":
                current_section = self.__parse(current_section)

                # after_branch, branch_2 = self.parse_next_branch()
            else:
                raise Exception("Not yet implemented for:" + self.__next_bracket())
            do_while = self.__next_bracket() == "(" or self.__next_bracket() == "|"

        branches.append(current_section)
        self.__move_till_after_next_bracket()
        after_branch = self.parse()

        return BranchedSection(
            before_branch,
            branches,
            after_branch
        )

    def parse_next_branch(self):
        self.__guard("|")
        if self.__next_bracket() == ")":
            branch_2 = self.__get_next_straight_section()
            self.__move_till_after_next_bracket()

            after_branch = self.parse_after_branch()
        elif self.__next_bracket() == "(":
            branch_2 = self.parse()

            after_branch = self.parse_after_branch()
        else:
            raise Exception("Not yet implemented for:" + self.__next_bracket())
        return after_branch, branch_2

    def parse_after_branch(self):
        if self.__next_bracket() == "$" or self.__next_bracket() == "|" or self.__next_bracket() == ")":
            after_branch = self.__get_next_straight_section()
            self.__move_till_after_next_bracket()
        elif self.__next_bracket() == "(":
            after_branch = self.parse()
        else:
            raise Exception("Not yet implemented for:" + self.__next_bracket())
        return after_branch


def parse_input_for_brackets(input_string: str) -> Section:
    return Commands(input_string).parse()

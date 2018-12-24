import unittest

from solutions.day20.BracketParsing import StraightSection, parse_input_for_brackets, BranchedSection


class TestBracketParsing(unittest.TestCase):
    def test_no_brackets(self):
        self.assertEqual(
            StraightSection("NWES"),
            parse_input_for_brackets("^NWES$")
        )

    def test_one_bracket(self):
        self.assertEqual(
            BranchedSection(StraightSection("N"), [StraightSection("W"), StraightSection("E")], StraightSection("S")),
            parse_input_for_brackets("^N(W|E)S$")
        )

    def test_two_brackets(self):
        self.assertEqual(
            BranchedSection(
                StraightSection("N"),
                [
                    StraightSection("W"),
                    StraightSection("E")
                ],
                BranchedSection(
                    StraightSection("S"), [StraightSection("N"), StraightSection("S")], StraightSection("W")
                )
            ),
            parse_input_for_brackets("^N(W|E)S(N|S)W$")
        )

    def test_nested_brackets_branch_1(self):
        self.assertEqual(
            BranchedSection(
                StraightSection("N"),
                [
                    BranchedSection(
                        StraightSection("S"), [StraightSection("N"), StraightSection("S")], StraightSection("W")
                    ),
                    StraightSection("W")
                ],
                StraightSection("E")
            ),
            parse_input_for_brackets("^N(S(N|S)W|W)E$")
        )

    def test_nested_brackets_branch_2(self):
        self.assertEqual(
            BranchedSection(
                StraightSection("N"),
                [
                    StraightSection("W"),
                    BranchedSection(
                        StraightSection("S"), [StraightSection("N"), StraightSection("S")], StraightSection("W")
                    )
                ],
                StraightSection("E")
            ),
            parse_input_for_brackets("^N(W|S(N|S)W)E$")
        )

    def test_3_option_branching(self):
        self.assertEqual(
            BranchedSection(
                StraightSection("S"),
                [
                    StraightSection("W"),
                    StraightSection("E"),
                    StraightSection("S")
                ],
                StraightSection("S")
            ),
            parse_input_for_brackets("^S(W|E|S)S$")
        )

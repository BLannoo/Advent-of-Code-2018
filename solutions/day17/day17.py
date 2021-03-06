import re
from typing import List

from solutions.utils.utils import grid_to_str, Location

SOURCE_X = 500


def parse_vein(vein_string: str) -> List[Location]:
    match_vertical = re.search("x=(\d+), y=(\d+)\.\.(\d+)", vein_string)
    if match_vertical:
        return [
            Location(int(match_vertical.group(1)), y)
            for y in range(int(match_vertical.group(2)), int(match_vertical.group(3)) + 1)
        ]
    match_horizontal = re.search("y=(\d+), x=(\d+)\.\.(\d+)", vein_string)
    if match_horizontal:
        return [
            Location(x, int(match_horizontal.group(1)))
            for x in range(int(match_horizontal.group(2)), int(match_horizontal.group(3)) + 1)
        ]
    raise Exception('vein_string did not match horizontal or vertical vein! vein_string:' + vein_string)


class Reservoir:
    __min_x: int
    __grid: List[List[str]]
    __focus: Location
    __focuses_to_retry: List[Location]
    __top_of_removed_water_falls: List[Location]

    def __init__(self, min_x: int, grid: List[List[str]]):
        self.__min_x = min_x
        self.__grid = grid
        self.__focus = Location(SOURCE_X - min_x, 0)
        self.__focuses_to_retry = []
        self.__top_of_removed_water_falls = [Location(-1, -1)]
        self.__bottom_of_removed_water_falls = [Location(-1, -1)]

    def flow(self, i: int):
        for temp in range(i):
            # print('flow iteration: ', temp)
            self.__flow()
            if len(self.__focuses_to_retry) == 0:
                return

    def __flow(self):
        if self.__grid[self.__focus.y + 1][self.__focus.x] != '.':

            if self.__grid[self.__focus.y + 1][self.__focus.x] == '|':
                tops_of_water_falls = [
                    tops
                    for tops in self.__top_of_removed_water_falls
                    if tops.y == self.__focus.y + 1
                ]
                if len(tops_of_water_falls) > 0:
                    non_water_tiles_between_top_of_water_fall_and_flowing_water_hit_by_focus = [
                        0
                        for x in range(tops_of_water_falls[0].x, self.__focus.x)
                        if self.__grid[tops_of_water_falls[0].y][x] != '|'
                    ]
                    if len(non_water_tiles_between_top_of_water_fall_and_flowing_water_hit_by_focus) == 0:
                        self.remove_water_fall(self.__focus)
                        if len(self.__focuses_to_retry) == 0:
                            return
                        self.__focus = self.__backtrace_to_get_new_focus()

            # print('space bellow (', self.__focus, ') is taken')
            if self.__grid[self.__focus.y][self.__focus.x - 1] != '.':
                # print('space left (', self.__focus, ') is taken')
                if self.__grid[self.__focus.y][self.__focus.x + 1] != '.':
                    # print('space right (', self.__focus, ') is taken')
                    self.__focus = self.__backtrace_to_get_new_focus()
                    if len(self.__focuses_to_retry) == 0:
                        return
                    # print('returning to: ', self.__focus)
                    self.__flow()
                    if len(self.__focuses_to_retry) == 0:
                        return
                else:
                    self.__change_focus(Location(self.__focus.x + 1, self.__focus.y))
            else:
                self.__change_focus(Location(self.__focus.x - 1, self.__focus.y))
        else:
            self.__change_focus(Location(self.__focus.x, self.__focus.y + 1))

        self.__grid[self.__focus.y][self.__focus.x] = '|'

        if self.__focus.y == len(self.__grid) - 1:
            self.remove_water_fall(self.__focus)
            if len(self.__focuses_to_retry) == 0:
                return
            self.__focus = self.__backtrace_to_get_new_focus()

    def __backtrace_to_get_new_focus(self):
        potential_new_focus = self.__focuses_to_retry.pop()
        if potential_new_focus.y < self.__top_of_removed_water_falls[-1].y:
            self.remove_water_fall(potential_new_focus)
            if len(self.__focuses_to_retry) == 0:
                print("Finished filling: water reached ", self.count_water(), " tiles")
                return
            potential_new_focus = self.__backtrace_to_get_new_focus()
        return potential_new_focus

    def remove_water_fall(self, bottom_of_fall: Location):
        self.__bottom_of_removed_water_falls.append(bottom_of_fall)
        top_of_fall = bottom_of_fall
        while bottom_of_fall.x == self.__focuses_to_retry[-1].x:
            top_of_fall = self.__focuses_to_retry.pop()
            if top_of_fall.y == 0:
                break
        self.__top_of_removed_water_falls.append(top_of_fall)

    def __change_focus(self, location: Location):
        self.__focuses_to_retry.append(self.__focus)
        self.__focus = location

    def __repr__(self) -> str:
        return grid_to_str(self.__grid)

    def count_water(self):
        return str(self).count('|')

    def dry(self):
        for water_fall_bottom, water_fall_top in zip(
                self.__bottom_of_removed_water_falls[1:],
                self.__top_of_removed_water_falls[1:]
        ):
            for y in range(water_fall_top.y, water_fall_bottom.y + 1):
                self.__grid[y][water_fall_bottom.x] = "."

            x_top_fall = water_fall_top.x
            y_top_fall = water_fall_top.y
            x = x_top_fall + 1
            while x < len(self.__grid[y_top_fall]) and self.__grid[y_top_fall][x] == '|':
                self.__grid[y_top_fall][x] = '.'
                x += 1
            x = x_top_fall - 1
            while x > 0 and self.__grid[y_top_fall][x] == '|':
                self.__grid[y_top_fall][x] = '.'
                x -= 1


def scan_input(input_string: str) -> Reservoir:
    veins: List[Location] = [
        vein
        for vein_string in input_string.split('\n')
        for vein in parse_vein(vein_string)
    ]
    min_x = min(min([vein.x for vein in veins]), SOURCE_X) - 1
    max_x = max(max([vein.x for vein in veins]), SOURCE_X) + 1
    max_y = max([vein.y for vein in veins])

    grid = [
        ['.' for _ in range(max_x - min_x + 1)]
        for _ in range(max_y + 1)
    ]

    for clay in veins:
        grid[clay.y][clay.x - min_x] = '#'

    grid[0][SOURCE_X - min_x] = '+'

    return Reservoir(min_x, grid)


if __name__ == "__main__":
    with open("../../data/day17.txt", "r") as file:
        reservoir = scan_input("".join(file.readlines()).strip())

    reservoir.flow(40000)
    print(reservoir)

# PART I

# guess: 37477 is too low -- issues with falling into flowing water
# guess: 38026 is too high -- no trace of error in print (reservoir.flow(40000); print(reservoir))
# guess: 38025 is too high -- not off by one error
# correct: 38021 -- 5 first rows are above top clay row

# PART II

# guess: 31964 is to low -- removing water from parallel streams

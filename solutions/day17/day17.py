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

    def __init__(self, min_x: int, grid: List[List[str]]):
        self.__min_x = min_x
        self.__grid = grid
        self.__focus = Location(SOURCE_X - min_x, 0)
        self.__focuses_to_retry = []

    def flow(self, i: int):
        for temp in range(i):
            self.__flow()

    def __flow(self):
        if self.__grid[self.__focus.y + 1][self.__focus.x] != '.':
            print('space bellow (', self.__focus, ') is taken')
            if self.__grid[self.__focus.y][self.__focus.x - 1] != '.':
                print('space left (', self.__focus, ') is taken')
                if self.__grid[self.__focus.y][self.__focus.x + 1] != '.':
                    print('space right (', self.__focus, ') is taken')
                    self.__focus = self.__focuses_to_retry.pop()  # take the previous one
                    print('returning to: ', self.__focus)
                    self.__flow()
                else:
                    self.__change_focus(Location(self.__focus.x + 1, self.__focus.y))
            else:
                self.__change_focus(Location(self.__focus.x - 1, self.__focus.y))
        else:
            self.__change_focus(Location(self.__focus.x, self.__focus.y + 1))

        self.__grid[self.__focus.y][self.__focus.x] = '|'

        if self.__focus.y == len(self.__grid) - 1:
            top_of_fall = self.remove_water_fall(self.__focus)
            self.__focus = self.__focuses_to_retry.pop()

    def remove_water_fall(self, bottom_of_fall: Location) -> Location:
        top_of_fall = bottom_of_fall
        while bottom_of_fall.x == self.__focuses_to_retry[-1].x:
            top_of_fall = self.__focuses_to_retry.pop()
        return top_of_fall

    def __change_focus(self, location: Location):
        self.__focuses_to_retry.append(self.__focus)
        self.__focus = location

    def __repr__(self) -> str:
        return grid_to_str(self.__grid)


def scan_input(input_string: str) -> Reservoir:
    veins: List[Location] = [
        vein
        for vein_string in input_string.split('\n')
        for vein in parse_vein(vein_string)
    ]
    min_x = min(min([vein.x for vein in veins]), SOURCE_X)
    max_x = max(max([vein.x for vein in veins]), SOURCE_X)
    max_y = max([vein.y for vein in veins])

    grid = [
        ['.' for _ in range(max_x - min_x + 1)]
        for _ in range(max_y + 1)
    ]

    for clay in veins:
        grid[clay.y][clay.x - min_x] = '#'

    grid[0][SOURCE_X - min_x] = '+'

    return Reservoir(min_x, grid)

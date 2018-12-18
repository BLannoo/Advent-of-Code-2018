import re
import unittest
from typing import List, Any

from solutions.utils.utils import grid_to_str, Location

SOURCE_X = 500

EXAMPLE_INPUT = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".strip()


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

    def flow(self, i):
        for _ in range(i):
            self.__flow()

    def __flow(self):
        if self.__grid[self.__focus.y + 1][self.__focus.x] != '.':
            print('space bellow taken: ', Location(self.__focus.x, self.__focus.y + 1))
            if self.__grid[self.__focus.y][self.__focus.x - 1] != '.':
                print('space left taken: ', Location(self.__focus.x - 1, self.__focus.y))
                self.__focus = self.__focuses_to_retry.pop()  # take the previous one
                print('returning to: ', self.__focus)
                self.__flow()
            else:
                self.__change_focus(Location(self.__focus.x - 1, self.__focus.y))
        else:
            self.__change_focus(Location(self.__focus.x, self.__focus.y + 1))
        self.__grid[self.__focus.y][self.__focus.x] = '|'

    def __change_focus(self, location):
        self.__focuses_to_retry.append(self.__focus)
        self.__focus = location

    def __repr__(self):
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


class TestDay17(unittest.TestCase):
    def test_render_vertical_vein(self):
        self.assertEqual(
            str(scan_input("x=495, y=2..7")),
            """
            .....+
            ......
            #.....
            #.....
            #.....
            #.....
            #.....
            #.....
            """.strip().replace(" ", "")
        )

    def test_render_horizontal_vein(self):
        self.assertEqual(
            str(scan_input("y=7, x=495..501")),
            """
            .....+.
            .......
            .......
            .......
            .......
            .......
            .......
            #######
            """.strip().replace(" ", "")
        )

    def test_render_example(self):
        self.assertEqual(
            str(scan_input(EXAMPLE_INPUT)),
            """
            .....+......
            ...........#
            #..#.......#
            #..#..#.....
            #..#..#.....
            #.....#.....
            #.....#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_1(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(1)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.......#
            #..#..#.....
            #..#..#.....
            #.....#.....
            #.....#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_2(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(2)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#..#.....
            #..#..#.....
            #.....#.....
            #.....#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_6(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(6)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #....|#.....
            #....|#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_7(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(7)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #....|#.....
            #...||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_10(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(10)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #....|#.....
            #|||||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_11(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(11)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #...||#.....
            #|||||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_12(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(12)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #..|||#.....
            #|||||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_14(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(14)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#.|#.....
            #|||||#.....
            #|||||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

    def test_flow_step_15(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(15)
        self.assertEqual(
            str(reservoir),
            """
            .....+......
            .....|.....#
            #..#.|.....#
            #..#.|#.....
            #..#||#.....
            #|||||#.....
            #|||||#.....
            #######.....
            ............
            ............
            ...#.....#..
            ...#.....#..
            ...#.....#..
            ...#######..
            """.strip().replace(' ', '')
        )

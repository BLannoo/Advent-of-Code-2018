import unittest
from typing import List

from solutions.utils.utils import grid_to_str, Location


def to_coordinates(room_location: Location) -> Location:
    return Location(room_location.x * 2 + 1, room_location.y * 2 + 1)


class Map:
    __grid: List[List[str]]

    def __init__(self, grid: List[List[str]]):
        self.__grid = grid

    def __repr__(self):
        return grid_to_str(self.__grid)

    def add_door_north_of(self, location: Location):
        coordinates = to_coordinates(location)
        self.__grid[coordinates.y - 1][coordinates.x] = "-"

    def add_door_west_of(self, location: Location):
        coordinates = to_coordinates(location)
        self.__grid[coordinates.y][coordinates.x - 1] = "|"

    def add_door_south_of(self, location: Location):
        coordinates = to_coordinates(location)
        self.__grid[coordinates.y + 1][coordinates.x] = "-"

    def add_door_east_of(self, location: Location):
        coordinates = to_coordinates(location)
        self.__grid[coordinates.y][coordinates.x + 1] = "|"


def create_base_grid(radius: int) -> List[List[str]]:
    number_of_rooms_side_by_side = radius * 2 + 1
    grid = [
        ["#" for _ in range(number_of_rooms_side_by_side * 2 + 1)]
        for _ in range(number_of_rooms_side_by_side * 2 + 1)
    ]
    for x in range(number_of_rooms_side_by_side):
        for y in range(number_of_rooms_side_by_side):
            grid[y * 2 + 1][x * 2 + 1] = "."
    return grid


def initiate_map(radius: int) -> Map:
    grid = create_base_grid(radius)
    start = to_coordinates(Location(radius, radius))
    grid[start.y][start.x] = "X"
    return Map(grid)


def scan_input(radius: int, string_input: str) -> Map:
    base_map = initiate_map(radius)
    direction = string_input[1]
    if direction == "N":
        base_map.add_door_north_of(Location(radius, radius))
    if direction == "W":
        base_map.add_door_west_of(Location(radius, radius))
    if direction == "S":
        base_map.add_door_south_of(Location(radius, radius))
    if direction == "E":
        base_map.add_door_east_of(Location(radius, radius))
    return base_map


class TestDay20(unittest.TestCase):
    def test_single_step_N_map(self):
        self.assertEqual(
            str(scan_input(1, "^N$")),
            """
            #######
            #.#.#.#
            ###-###
            #.#X#.#
            #######
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

    def test_single_step_W_map(self):
        self.assertEqual(
            str(scan_input(1, "^W$")),
            """
            #######
            #.#.#.#
            #######
            #.|X#.#
            #######
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

    def test_single_step_S_map(self):
        self.assertEqual(
            str(scan_input(1, "^S$")),
            """
            #######
            #.#.#.#
            #######
            #.#X#.#
            ###-###
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

    def test_single_step_E_map(self):
        self.assertEqual(
            str(scan_input(1, "^E$")),
            """
            #######
            #.#.#.#
            #######
            #.#X|.#
            #######
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

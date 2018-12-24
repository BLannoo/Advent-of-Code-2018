from typing import List

from solutions.day20.BracketParsing import parse_input_for_brackets, Section, StraightSection
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

    def add_door(self, direction: str, location: Location):
        if direction == "N":
            self.add_door_north_of(location)
        if direction == "W":
            self.add_door_west_of(location)
        if direction == "S":
            self.add_door_south_of(location)
        if direction == "E":
            self.add_door_east_of(location)

    # adds doors AND returns end location
    def follow_commands(self, locations: List[Location], brackets: Section):
        brackets.follow_commands(locations, self)

    def follow_basic_commands(self, location: Location, commands: str) -> Location:
        for direction in commands:
            if direction not in ['N', 'W', 'S', 'E']:
                raise Exception("direction must be in (N, E, S, W) but was: " + direction)
            self.add_door(direction, location)
            location = location.move(direction)
        return location

    def follow_basic_command_lists(self, commands: str, locations: List[Location]) -> List[Location]:
        new_locations = []
        for location in locations:
            new_locations.append(self.follow_basic_commands(location, commands))
        return new_locations


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


def move(direction: str, location: Location) -> Location:
    if direction == "N":
        location = Location(location.x, location.y - 1)
    if direction == "W":
        location = Location(location.x - 1, location.y)
    if direction == "S":
        location = Location(location.x, location.y + 1)
    if direction == "E":
        location = Location(location.x + 1, location.y)
    return location


def scan_input(radius: int, string_input: str) -> Map:

    brackets = parse_input_for_brackets(string_input)
    map_layout = initiate_map(radius)
    locations = [Location(radius, radius)]

    map_layout.follow_commands(locations, brackets)

    return map_layout

from typing import List, Set

from solutions.day20.BracketParsing import parse_input_for_brackets, Section
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
    def follow_commands(self, locations: Set[Location], brackets: Section):
        brackets.follow_commands(locations, self)

    def follow_basic_commands(self, location: Location, commands: str) -> Location:
        for direction in commands:
            if direction not in ['N', 'W', 'S', 'E']:
                raise Exception("direction must be in (N, E, S, W) but was: " + direction)
            self.add_door(direction, location)
            location = location.move(direction)
        return location

    def follow_basic_command_lists(self, commands: str, locations: Set[Location]) -> Set[Location]:
        new_locations = set()
        for location in locations:
            new_locations |= {self.follow_basic_commands(location, commands)}
        return new_locations

    def size(self, start: Location):

        visited_rooms = [start]
        current_rooms = [start]
        next_rooms = []
        step = -1
        while len(current_rooms) > 0:
            step += 1
            for room in current_rooms:
                next_rooms.extend([
                    next_room
                    for next_room in self.find_accessible_rooms(room)
                    if not visited_rooms.__contains__(next_room)
                ])
            visited_rooms.extend(next_rooms)
            current_rooms = next_rooms
            next_rooms = []

        return step

    def find_accessible_rooms(self, room) -> List[Location]:
        return [
            neighbour
            for neighbour in room.neighbours4()
            if self.has_door(room, neighbour)
        ]

    def has_door(self, room, neighbour) -> bool:
        room_coords = to_coordinates(room)
        neighbour_coords = to_coordinates(neighbour)

        if room_coords.x == neighbour_coords.x:
            y = int(abs(room_coords.y + neighbour_coords.y) / 2)
            return self.__grid[y][room_coords.x] in ["|", "-"]
        elif room_coords.y == neighbour_coords.y:
            x = int(abs(room_coords.x + neighbour_coords.x) / 2)
            return self.__grid[room_coords.y][x] in ["|", "-"]
        else:
            raise Exception('Doors can only be checked between neighbouring rooms')


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
    locations = {Location(radius, radius)}

    map_layout.follow_commands(locations, brackets)

    return map_layout


if __name__ == "__main__":
    with open("../../data/day20.txt", "r") as file:
        input_string = file.readline()

    SIZE = 52

    actual_brackets = parse_input_for_brackets(input_string)

    actual_map_layout = initiate_map(SIZE)

    initial_locations = {Location(SIZE, SIZE)}

    actual_map_layout.follow_commands(initial_locations, actual_brackets)

    print(actual_map_layout)

    print(actual_map_layout.size(Location(SIZE, SIZE)))


# Part I
# 4011 answer is to low -- grid was to small (50) -- grid 52 is perfect
# 4184 correct

from typing import List


def load_data_for_day(day):
    file_name = '../data/day' + str(day) + '.txt'

    data = list([])

    with open(file_name, 'r') as data_file:
        for line in data_file:
            data.append(line.strip())

    return data


def str_to_grid(input_string: str) -> List[List[str]]:
    return [list(line) for line in input_string.strip().split('\n')]


def grid_to_str(grid: List[List[str]]) -> str:
    return '\n'.join([''.join(cells) for cells in grid])


DIRECTIONS_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIRECTIONS_8 = [
    (1, 0), (0, 1), (-1, 0), (0, -1),
    (1, 1), (-1, 1), (1, -1), (-1, -1)
]


class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def neighbours4(self) -> List['Location']:
        return [
            Location(self.x + direction[0], self.y + direction[1])
            for direction in DIRECTIONS_4
        ]

    def neighbours8(self) -> List['Location']:
        return [
            Location(self.x + direction[0], self.y + direction[1])
            for direction in DIRECTIONS_8
        ]

    def __lt__(self, other: 'Location') -> bool:
        if self.y < other.y:
            return True
        else:
            return self.x < other.x

    def __gt__(self, other: 'Location') -> bool:
        if self.y > other.y:
            return True
        else:
            return self.x > other.x

    def __eq__(self, other: 'Location') -> bool:
        return self.x == other.x and self.y == other.y

    def __le__(self, other: 'Location') -> bool:
        return not self.__gt__(other)

    def __ge__(self, other: 'Location') -> bool:
        return not self.__lt__(other)

    def __ne__(self, other: 'Location') -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return 'Location(x=' + str(self.x) + ', y=' + str(self.y) + ')'

    def move(self, direction):
        if direction == "N":
            return Location(self.x, self.y - 1)
        if direction == "W":
            return Location(self.x - 1, self.y)
        if direction == "S":
            return Location(self.x, self.y + 1)
        if direction == "E":
            return Location(self.x + 1, self.y)


def filter_outside(locations: List[Location], max_inclusive, min_inclusive=0) -> List[Location]:
    return [
        loc for loc in locations
        if (
                min_inclusive <= loc.x <= max_inclusive
                and
                min_inclusive <= loc.y <= max_inclusive
        )
    ]

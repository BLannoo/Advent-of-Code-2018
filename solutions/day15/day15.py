import unittest
from copy import deepcopy
from typing import List


def grid_to_str(grid):
    return '\n'.join([''.join(cells) for cells in grid])


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Location(x=' + str(self.x) + ', y=' + str(self.y) + ')'


SMALL_CAVE: str = """
#######
#.G.E.#
#E.G.E#
#.G.E.#
#######
""".strip()

SMALL_CAVE_MAP: str = """
#######
#.....#
#.....#
#.....#
#######
""".strip()


class Creature:
    def __init__(self, creature_type: str, loc: Location):
        self.loc = loc
        self.creature_type = creature_type

    def __eq__(self, other):
        return (
                self.creature_type == other.creature_type
                and
                self.loc == other.loc
        )

    def __repr__(self):
        return (
                'Creature(' +
                'creature_type=' + self.creature_type + ', ' +
                'loc=' + str(self.loc) + ')'
        )


class Cave:

    def __init__(self, cave_map: List[List[str]], creatures: List[Creature]):
        self.creatures = creatures
        self.cave_map = cave_map

    def __str__(self):
        cave = deepcopy(self.cave_map)
        for creature in self.creatures:
            cave[creature.loc.y][creature.loc.x] = creature.creature_type
        return grid_to_str(cave)


def scan_input(input_string: str):
    cave_map = [list(line) for line in input_string.strip().split('\n')]
    creatures = []
    for x in range(len(cave_map)):
        for y in range(len(cave_map[x])):
            if cave_map[x][y] == 'E' or cave_map[x][y] == 'G':
                creatures.append(Creature(cave_map[x][y], Location(y, x)))
                cave_map[x][y] = '.'
    return Cave(cave_map, creatures)


class TestDay15(unittest.TestCase):

    def test_small_cave_map_can_be_extracted(self):
        self.assertEqual(
            grid_to_str(scan_input(SMALL_CAVE).cave_map),
            SMALL_CAVE_MAP
        )

    def test_small_cave_creatures_can_be_extracted(self):
        self.assertEqual(
            scan_input(SMALL_CAVE).creatures,
            [
                Creature('G', Location(2, 1)),
                Creature('E', Location(4, 1)),
                Creature('E', Location(1, 2)),
                Creature('G', Location(3, 2)),
                Creature('E', Location(5, 2)),
                Creature('G', Location(2, 3)),
                Creature('E', Location(4, 3))
            ]
        )

    def test_small_cave_str_returns_input(self):
        self.assertEqual(
            str(scan_input(SMALL_CAVE)),
            SMALL_CAVE
        )

from copy import deepcopy
from typing import List

from solutions.utils.utils import grid_to_str, Location


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

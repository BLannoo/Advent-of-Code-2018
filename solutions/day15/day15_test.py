import unittest

from solutions.utils.utils import grid_to_str, Location
from solutions.day15.day15 import scan_input, Creature

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


class TestSmallCave(unittest.TestCase):
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


DESTINATION_PRACTICE_CAVE: str = """
#######
#E..G.#
#...#.#
#.G.#G#
#######
""".strip()


class TestDestination(unittest.TestCase):
    def test_find_targets(self):
        self.assertEqual(
            scan_input(DESTINATION_PRACTICE_CAVE).find_targets(Creature('E', Location(1, 1))),
            [
                Location(4, 1),
                Location(2, 3),
                Location(5, 3)
            ]
        )

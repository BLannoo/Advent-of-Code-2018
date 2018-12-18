import unittest

from solutions.day18.day18 import scan_input

EXTENDED_EXAMPLE = """
            .#.#...|#.
            .....#|##|
            .|..|...#.
            ..|#.....#
            #.#|||#|#|
            ...#.||...
            .|....|...
            ||...#|.#|
            |.||||..|.
            ...#.|..|.
            """.strip().replace(' ', '')

SIMPLE_AREA = """
...
###
|||
""".strip()

PURE_TREES = """
|||
|||
|||
""".strip()

PURE_OPEN = """
...
...
...
""".strip()

PURE_LUMBERYARD = """
###
###
###
""".strip()


class TestDay18(unittest.TestCase):
    def test_scan_and_print(self):
        self.assertEqual(
            str(scan_input(SIMPLE_AREA)),
            SIMPLE_AREA
        )

    def test_trees_stays_trees(self):
        area = scan_input(PURE_TREES)
        area.tic(10)
        self.assertEqual(
            str(area),
            PURE_TREES
        )

    def test_open_stays_open(self):
        area = scan_input(PURE_OPEN)
        area.tic(10)
        self.assertEqual(
            str(area),
            PURE_OPEN
        )

    def test_lumberyard_turns_into_open(self):
        area = scan_input(PURE_LUMBERYARD)
        area.tic(10)
        self.assertEqual(
            str(area),
            PURE_OPEN
        )

    def test_open_with_3_neighbouring_trees_turn_into_trees(self):
        area = scan_input(
            """
            |||
            ...
            ...
            """.strip().replace(' ', '')
        )
        area.tic(1)
        self.assertEqual(
            str(area),
            """
            |||
            .|.
            ...
            """.strip().replace(' ', '')
        )

    def test_trees_with_3_neighbouring_lumberyards_turn_into_lumberyard(self):
        area = scan_input(
            """
            ###
            |||
            |||
            """.strip().replace(' ', '')
        )
        area.tic(1)
        self.assertEqual(
            str(area),
            """
            ###
            |#|
            |||
            """.strip().replace(' ', '')
        )

    def test_example_1min(self):
        area = scan_input(
            EXTENDED_EXAMPLE
        )
        area.tic(1)
        self.assertEqual(
            str(area),
            """
            .......##.
            ......|###
            .|..|...#.
            ..|#||...#
            ..##||.|#|
            ...#||||..
            ||...|||..
            |||||.||.|
            ||||||||||
            ....||..|.
            """.strip().replace(' ', '')
        )

    def test_example_10min(self):
        area = scan_input(
            EXTENDED_EXAMPLE
        )
        area.tic(10)
        self.assertEqual(
            str(area),
            """
            .||##.....
            ||###.....
            ||##......
            |##.....##
            |##.....##
            |##....##|
            ||##.####|
            ||#####|||
            ||||#|||||
            ||||||||||
            """.strip().replace(' ', '')
        )

    def test_count_trees(self):
        area = scan_input(
            EXTENDED_EXAMPLE
        )
        area.tic(10)
        self.assertEqual(area.count('|'), 37)
        self.assertEqual(area.count('#'), 31)
        self.assertEqual(area.resource_value(), 1147)

    def test_part_1(self):
        with open('../../data/day18.txt', 'r') as file:
            area = scan_input(''.join(file.readlines()))
            area.tic(10)
            self.assertEqual(area.resource_value(), 545600)

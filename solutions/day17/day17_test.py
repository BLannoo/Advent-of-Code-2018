import unittest

from solutions.day17.day17 import scan_input, Reservoir

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


class TestDay17(unittest.TestCase):
    def test_render_vertical_vein(self):
        self.assertEqual(
            str(scan_input("x=495, y=2..7")),
            """
            ......+.
            ........
            .#......
            .#......
            .#......
            .#......
            .#......
            .#......
            """.strip().replace(" ", "")
        )

    def test_render_horizontal_vein(self):
        self.assertEqual(
            str(scan_input("y=7, x=495..501")),
            """
            ......+..
            .........
            .........
            .........
            .........
            .........
            .........
            .#######.
            """.strip().replace(" ", "")
        )

    def test_render_example(self):
        self.assertEqual(
            str(scan_input(EXAMPLE_INPUT)),
            """
            ......+.......
            ............#.
            .#..#.......#.
            .#..#..#......
            .#..#..#......
            .#.....#......
            .#.....#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_1(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(1)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.......#.
            .#..#..#......
            .#..#..#......
            .#.....#......
            .#.....#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_2(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(2)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#..#......
            .#..#..#......
            .#.....#......
            .#.....#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_6(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(6)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#....|#......
            .#....|#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_7(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(7)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#....|#......
            .#...||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_10(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(10)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#....|#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_11(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(11)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#...||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_12(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(12)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#..|||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_14(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(14)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#.|#......
            .#|||||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_15(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(15)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#.|.....#.
            .#..#.|#......
            .#..#||#......
            .#|||||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_17(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(17)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||.....#.
            .#..#||#......
            .#..#||#......
            .#|||||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_18(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(18)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#|||....#.
            .#..#||#......
            .#..#||#......
            .#|||||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_19(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(19)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#......
            .#..#||#......
            .#|||||#......
            .#|||||#......
            .#######......
            ..............
            ..............
            ....#.....#...
            ....#.....#...
            ....#.....#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_29(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(29)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ........|.....
            ....#...|.#...
            ....#...|.#...
            ....#...|.#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_41(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(41)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ........|.....
            ....#|||||#...
            ....#|||||#...
            ....#|||||#...
            ....#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_50(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(50)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ...||||||.....
            ...|#|||||#...
            ...|#|||||#...
            ...|#|||||#...
            ...|#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_51(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(51)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ...|||||||....
            ...|#|||||#...
            ...|#|||||#...
            ...|#|||||#...
            ...|#######...
            """.strip().replace(' ', '')
        )

    def test_flow_step_57(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(57)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ...|||||||||..
            ...|#|||||#|..
            ...|#|||||#|..
            ...|#|||||#|..
            ...|#######|..
            """.strip().replace(' ', '')
        )

    # should be same as 57
    def test_flow_step_58(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(58)
        self.assertEqual(
            str(reservoir),
            """
            ......+.......
            ......|.....#.
            .#..#||||...#.
            .#..#||#|.....
            .#..#||#|.....
            .#|||||#|.....
            .#|||||#|.....
            .#######|.....
            ........|.....
            ...|||||||||..
            ...|#|||||#|..
            ...|#|||||#|..
            ...|#|||||#|..
            ...|#######|..
            """.strip().replace(' ', '')
        )

    def test_count_water(self):
        reservoir: Reservoir = scan_input(EXAMPLE_INPUT)
        reservoir.flow(58)
        self.assertEqual(
            reservoir.count_water(),
            57
        )
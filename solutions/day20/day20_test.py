import unittest

from solutions.day20.day20 import scan_input


class TestDay20(unittest.TestCase):
    def test_single_step_N(self):
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

    def test_single_step_W(self):
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

    def test_single_step_S(self):
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

    def test_single_step_E(self):
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

    def test_two_steps_NE(self):
        self.assertEqual(
            str(scan_input(1, "^NE$")),
            """
            #######
            #.#.|.#
            ###-###
            #.#X#.#
            #######
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

    def test_full_circle_steps(self):
        self.assertEqual(
            str(scan_input(1, "^NESSWWNNE$")),
            """
            #######
            #.|.|.#
            #-#-#-#
            #.#X#.#
            #-###-#
            #.|.|.#
            #######
            """.strip().replace(" ", "")
        )

    def test_two_paths_EiNSoW(self):
        self.assertEqual(
            str(scan_input(1, "^E(N|S)W$")),
            """
            #######
            #.#.|.#
            #####-#
            #.#X|.#
            #####-#
            #.#.|.#
            #######
            """.strip().replace(" ", "")
        )

    def test_two_consecutive_branches(self):
        self.assertEqual(
            str(scan_input(2, "^E(N|S)W(N|W)W$")),
            """
            ###########
            #.#.|.#.#.#
            #####-#####
            #.|.|.|.#.#
            #######-###
            #.#.|X|.#.#
            #####-#-###
            #.|.|.|.#.#
            ###########
            #.#.#.#.#.#
            ###########
            """.strip().replace(" ", "")
        )

    def test_empty_branches(self):
        self.assertEqual(
            str(scan_input(2, "^E(N|)E$")),
            """
            ###########
            #.#.#.#.#.#
            ###########
            #.#.#.#.|.#
            #######-###
            #.#.#X|.|.#
            ###########
            #.#.#.#.#.#
            ###########
            #.#.#.#.#.#
            ###########
            """.strip().replace(" ", "")
        )

    def todo_test_nested_branches(self):
        self.assertEqual(
            str(scan_input(2, "^E(N|(S|))E$")),
            """
            ###########
            #.#.#.#.#.#
            ###########
            #.#.#.#.|.#
            #######-###
            #.#.#X|.|.#
            #######-###
            #.#.#.#.|.#
            ###########
            #.#.#.#.#.#
            ###########
            """.strip().replace(" ", "")
        )

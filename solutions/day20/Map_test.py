import unittest

from solutions.day20.day20 import scan_input
from solutions.utils.utils import Location


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

    def test_nested_branches(self):
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

    def test_example_in_assignment(self):
        self.assertEqual(
            str(scan_input(2, "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$")),
            """
            ###########
            #.|.#.|.#.#
            #-###-#-#-#
            #.|.|.#.#.#
            #-#####-#-#
            #.#.#X|.#.#
            #-#-#####-#
            #.#.|.|.|.#
            #-###-###-#
            #.|.|.#.|.#
            ###########
            """.strip().replace(" ", "")
        )

    def test_size_of_small_map(self):
        self.assertEqual(
            3,
            scan_input(1, "^WNE$").size(Location(1, 1))
        )

    def test_size_of_second_example_map(self):
        self.assertEqual(
            10,
            scan_input(2, "^ENWWW(NEEE|SSE(EE|N))$").size(Location(2, 2))
        )

    def test_size_of_third_example_map(self):
        self.assertEqual(
            18,
            scan_input(2, "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$").size(Location(2, 2))
        )

    def test_size_of_fourth_example_map(self):
        self.assertEqual(
            23,
            scan_input(3, "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$").size(Location(3, 3))
        )

    def test_size_of_fifth_example_map(self):
        self.assertEqual(
            31,
            scan_input(3, "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$").size(Location(3, 3))
        )

    def test_triple_path(self):
        self.assertEqual(
            str(scan_input(1, "^(|W|E)S$")),
            """
            #######
            #.#.#.#
            #######
            #.|X|.#
            #-#-#-#
            #.#.#.#
            #######
            """.strip().replace(" ", "")
        )

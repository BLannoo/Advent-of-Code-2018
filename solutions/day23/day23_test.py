import unittest

from solutions.day23.day23 import Swarm, NanoBot, scan_nano_bots


class TestCaseDay23(unittest.TestCase):

    def test_create_swarm(self):
        self.assertCountEqual(
            Swarm(bots=[
                NanoBot(pos=(0, 0, 0), r=4),
                NanoBot(pos=(1, 0, 0), r=1),
                NanoBot(pos=(4, 0, 0), r=3),
                NanoBot(pos=(0, 2, 0), r=1),
                NanoBot(pos=(0, 5, 0), r=3),
                NanoBot(pos=(0, 0, 3), r=1),
                NanoBot(pos=(1, 1, 1), r=1),
                NanoBot(pos=(1, 1, 2), r=1),
                NanoBot(pos=(1, 3, 1), r=1)
            ]).bots,
            Swarm.create("""
            pos=<0,0,0>, r=4
            pos=<1,0,0>, r=1
            pos=<4,0,0>, r=3
            pos=<0,2,0>, r=1
            pos=<0,5,0>, r=3
            pos=<0,0,3>, r=1
            pos=<1,1,1>, r=1
            pos=<1,1,2>, r=1
            pos=<1,3,1>, r=1
            """.strip().replace("  ", "")).bots
        )

    def test_get_strongest(self):
        self.assertEqual(
            NanoBot(pos=(0, 0, 0), r=4),
            Swarm(bots=[
                NanoBot(pos=(0, 0, 0), r=4),
                NanoBot(pos=(1, 0, 0), r=1),
                NanoBot(pos=(4, 0, 0), r=3),
                NanoBot(pos=(0, 2, 0), r=1),
                NanoBot(pos=(0, 5, 0), r=3),
                NanoBot(pos=(0, 0, 3), r=1),
                NanoBot(pos=(1, 1, 1), r=1),
                NanoBot(pos=(1, 1, 2), r=1),
                NanoBot(pos=(1, 3, 1), r=1)
            ]).calc_strongest()
        )

    def test_count_in_range(self):
        self.assertEqual(
            7,
            Swarm(bots=[
                NanoBot(pos=(0, 0, 0), r=4),
                NanoBot(pos=(1, 0, 0), r=1),
                NanoBot(pos=(4, 0, 0), r=3),
                NanoBot(pos=(0, 2, 0), r=1),
                NanoBot(pos=(0, 5, 0), r=3),
                NanoBot(pos=(0, 0, 3), r=1),
                NanoBot(pos=(1, 1, 1), r=1),
                NanoBot(pos=(1, 1, 2), r=1),
                NanoBot(pos=(1, 3, 1), r=1)
            ]).in_range_of(NanoBot(pos=(0, 0, 0), r=4))
        )

    def test_count_in_range_with_negative_values(self):
        self.assertEqual(
            7,
            Swarm(bots=[
                NanoBot(pos=(-0, -0, -0), r=4),
                NanoBot(pos=(-1, -0, -0), r=1),
                NanoBot(pos=(-4, -0, -0), r=3),
                NanoBot(pos=(-0, -2, -0), r=1),
                NanoBot(pos=(-0, -5, -0), r=3),
                NanoBot(pos=(-0, -0, -3), r=1),
                NanoBot(pos=(-1, -1, -1), r=1),
                NanoBot(pos=(-1, -1, -2), r=1),
                NanoBot(pos=(-1, -3, -1), r=1)
            ]).in_range_of(NanoBot(pos=(0, 0, 0), r=4))
        )

    def test_part_I(self):
        swarm = scan_nano_bots()
        self.assertEqual(
            240,
            swarm.in_range_of(swarm.calc_strongest())
        )

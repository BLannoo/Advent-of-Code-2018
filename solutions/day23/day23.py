import re
import unittest
from typing import List


def manhattan(pos1: tuple, pos2: tuple) -> int:
    return (
            abs(pos1[0] - pos2[0])
            + abs(pos1[1] - pos2[1])
            + abs(pos1[2] - pos2[2])
    )


class NanoBot:
    def __init__(self, pos: tuple, r: int):
        self.r = r
        self.pos = pos

    @staticmethod
    def create(description) -> 'NanoBot':
        match = re.match("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", description)
        return NanoBot(
            pos=(int(match.group(1)), int(match.group(2)), int(match.group(3))),
            r=int(match.group(4))
        )

    def __eq__(self, other):
        return (
                isinstance(other, NanoBot)
                and
                self.pos == other.pos
                and
                self.r == other.r
        )

    def __repr__(self) -> str:
        return (
                "NanoBot(" +
                "pos=" + str(self.pos) + ", " +
                "r=" + str(self.r) + ")"
        )

    def distance(self, other):
        return manhattan(self.pos, other.pos)


class Swarm:
    def __init__(self, bots: List[NanoBot]):
        self.bots = bots

    @staticmethod
    def create(description: str) -> 'Swarm':
        bots = []
        for line in description.split("\n"):
            bots.append(NanoBot.create(line))
        return Swarm(bots)

    @staticmethod
    def create_from_file(file_name: str) -> 'Swarm':
        with open(file_name, "r") as file:
            return Swarm.create("".join(file.readlines()))

    def __eq__(self, other):
        return (
                self.bots == other.bots
        )

    def __repr__(self) -> str:
        return (
                "\nSwarm(bots=[\n\t" +
                ",\n\t".join([str(bot) for bot in self.bots]) +
                "\n])\n"
        )

    def calc_strongest(self):
        return max(self.bots, key=lambda bot: bot.r)

    def in_range_of(self, reference_bot: NanoBot):
        return len([
            bot for bot in self.bots
            if bot.distance(reference_bot) <= reference_bot.r
        ])

    def bots_in_range(self, point: tuple):
        return len([
            bot for bot in self.bots
            if manhattan(bot.pos, point) <= bot.r
        ])


def scan_nano_bots() -> Swarm:
    return Swarm.create_from_file("../../data/day23.txt")


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

    def test_part_II(self):
        swarm = scan_nano_bots()




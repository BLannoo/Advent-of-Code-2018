import re
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


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
        return sum(
            1 for bot in self.bots
            if manhattan(bot.pos, point) <= bot.r
        )

    def sort_by_radius(self):
        self.bots.sort(key=lambda bot: bot.r)

    def limit_swarm(self, reference_point, missing_distance):
        return Swarm([
            bot
            for bot in self.bots
            if abs(manhattan(bot.pos, reference_point) - bot.r) < missing_distance
        ])


def scan_nano_bots() -> Swarm:
    return Swarm.create_from_file("../../data/day23.txt")


def plot_swarm(swarm: Swarm, color):
    plot_positions([(*bot.pos, color(bot)) for bot in swarm.bots])


def plot_positions(data):
    fig = plt.figure(figsize=(16, 5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    cloud = ax.scatter(
        [data_point[0] for data_point in data],
        [data_point[1] for data_point in data],
        [data_point[2] for data_point in data],
        c=[data_point[3] for data_point in data],
        cmap=cm.coolwarm
    )
    ax.view_init(elev=45, azim=45)
    fig.colorbar(cloud, shrink=0.5, aspect=5)
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    cloud = ax.scatter(
        [data_point[0] for data_point in data],
        [data_point[1] for data_point in data],
        [data_point[2] for data_point in data],
        c=[data_point[3] for data_point in data],
        cmap=cm.coolwarm
    )
    ax.view_init(elev=-45, azim=45 + 180)
    fig.colorbar(cloud, shrink=0.5, aspect=5)
    plt.show()


def create_grid_within_bounds(old_positions, swarm: Swarm):
    x = np.linspace(
        min(old_positions, key=lambda pos: pos[0])[0],
        max(old_positions, key=lambda pos: pos[0])[0],
        20,
        dtype=int
    )
    y = np.linspace(
        min(old_positions, key=lambda pos: pos[1])[1],
        max(old_positions, key=lambda pos: pos[1])[1],
        20,
        dtype=int
    )
    z = np.linspace(
        min(old_positions, key=lambda pos: pos[2])[2],
        max(old_positions, key=lambda pos: pos[2])[2],
        20,
        dtype=int
    )
    new_positions = []
    for x_val in x:
        for y_val in y:
            for z_val in z:
                pos = (x_val, y_val, z_val)
                new_positions.append((*pos, swarm.bots_in_range(pos)))

    return new_positions


def select_pos_and_counts_bigger_then(pos_and_counts, min_counts: int):
    return [
        pos_and_count
        for pos_and_count in pos_and_counts
        if pos_and_count[3] >= min_counts
    ]


def report(pos, swarm):
    print("Point: ", pos, " has ", swarm.bots_in_range(pos), " bots in range!")


def hist_distance_deficit(reference_point, swarm):
    deficits = [
        manhattan(bot.pos, reference_point) - bot.r
        for bot in swarm.bots
    ]
    plt.hist(deficits, 100)
    plt.show()


if __name__ == "__main__":
    actual_swarm = scan_nano_bots()

    report((0, 0, 0), actual_swarm)

    bot_in_range_of_most_others = max(actual_swarm.bots, key=lambda bot: actual_swarm.bots_in_range(bot.pos))
    report(bot_in_range_of_most_others.pos, actual_swarm)

    hist_distance_deficit(bot_in_range_of_most_others.pos, actual_swarm)

    limited_swarm = actual_swarm.limit_swarm(bot_in_range_of_most_others.pos, 0.2e8)

    hist_distance_deficit(bot_in_range_of_most_others.pos, limited_swarm)


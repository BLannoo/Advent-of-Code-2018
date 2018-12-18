from copy import deepcopy

import matplotlib.pyplot as plt

from solutions.utils.utils import str_to_grid, grid_to_str, Location, filter_outside


class Area:
    def __init__(self, grid):
        self.grid = grid

    def tic(self, i):
        for _ in range(i):
            self.__tic()

    def __tic(self):
        old_grid = deepcopy(self.grid)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                adjecant_loc = filter_outside(Location(y, x).neighbours8(), len(self.grid) - 1)
                states = [old_grid[loc.x][loc.y] for loc in adjecant_loc]

                if old_grid[y][x] == '.' and states.count('|') >= 3:
                    self.grid[y][x] = '|'

                if old_grid[y][x] == '|' and states.count('#') >= 3:
                    self.grid[y][x] = '#'

                if old_grid[y][x] == '#' and (states.count('#') == 0 or states.count('|') == 0):
                    self.grid[y][x] = '.'

    def __repr__(self):
        return grid_to_str(self.grid)

    def count(self, state: str) -> int:
        return grid_to_str(self.grid).count(state)

    def resource_value(self):
        return self.count('|') * self.count('#')


def scan_input(input_string: str) -> Area:
    return Area(str_to_grid(input_string))


if __name__ == '__main__':
    with open('../../data/day18.txt', 'r') as file:
        area = scan_input(''.join(file.readlines()))

        resource_values = []
        for i in range(1000):
            area.tic(1)
            resource_values.append(area.resource_value())

    plt.plot(resource_values)
    plt.show()

    plt.plot(resource_values[950:])
    plt.show()

    min_res = min(resource_values[950:])
    min_index_last = resource_values[970:].index(min_res) + 970
    min_index_one_but_last = resource_values[950:970].index(min_res) + 950
    period = min_index_last - min_index_one_but_last

    print('answer:',
          resource_values[
              min_index_one_but_last
              + (1000000000 - min_index_last) % period
              - 1  # minute 1 is index 0
          ])

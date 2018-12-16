def load_data_for_day(day):
    file_name = '../data/day' + str(day) + '.txt'

    data = list([])

    with open(file_name, 'r') as data_file:
        for line in data_file:
            data.append(line.strip())

    return data


def grid_to_str(grid):
    return '\n'.join([''.join(cells) for cells in grid])


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Location(x=' + str(self.x) + ', y=' + str(self.y) + ')'
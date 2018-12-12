import numpy as np

from collections import defaultdict

SIZE = 300

cache = defaultdict(lambda: np.negative(np.ones((SIZE+1, SIZE+1), dtype=int)))


def power_level(x, y, serial_number):
    if cache[serial_number][x][y] == -1:
        rack_id = x + 10
        step_1 = rack_id * y
        step_2 = step_1 + serial_number
        step_3 = step_2 * rack_id
        step_4 = int(str(step_3)[-3])
        step_5 = step_4 - 5
        cache[serial_number][x][y] = step_5
    # print('x=', x, '; y=', y, '; p=', cache[x][y])
    return cache[serial_number][x][y]


print(power_level(3, 5, 8))
print(power_level(122, 79, 57))
print(power_level(217, 196, 39))
print(power_level(101, 153, 71))


def power_level_nxn(X, Y, serial_number, grid_size=3):
    total = 0
    for x in range(X, X + grid_size):
        for y in range(Y, Y + grid_size):
            total += power_level(x, y, serial_number)
    return total


def determine_power_level_change(X, Y, grid_size, serial_number):
    if grid_size == 0:
        return 0
    power_level_change = 0
    for x in range(X, X + grid_size - 1):
        power_level_change += power_level(x, Y + grid_size - 1, serial_number)
    for y in range(Y, Y + grid_size - 1):
        power_level_change += power_level(X + grid_size - 1, y, serial_number)
    power_level_change += power_level(X + grid_size - 1, Y + grid_size - 1, serial_number)
    return power_level_change


def temp(X, Y, serial_number):
    local_power_level = 0
    for grid_size in range(4):
        local_power_level += determine_power_level_change(X, Y, grid_size, serial_number)
    return local_power_level


print(temp(33, 45, 18))
print(temp(21, 61, 42))


def find_max_power_level(serial_number, min_grid_size=1, max_grid_size=300):
    max_power = 0
    X_max = 0
    Y_max = 0
    grid_size_max = 0
    for X in range(1, SIZE + 1):
        print('max found is: ', (X_max, Y_max, grid_size_max, max_power))
        print('trying X=', X)
        for Y in range(1, SIZE + 1):
            local_max_grid_size = min(SIZE + 1 - max(X, Y), max_grid_size)

            local_power_level = 0

            for grid_size in range(local_max_grid_size + 1):
                local_power_level += determine_power_level_change(X, Y, grid_size, serial_number)

                if local_power_level > max_power and grid_size >= min_grid_size:
                    max_power = local_power_level
                    X_max = X
                    Y_max = Y
                    grid_size_max = grid_size

    return X_max, Y_max, grid_size_max, max_power


# print(find_max_power_level(18, 15, 17))
# print(find_max_power_level(42, 11, 13))
print(find_max_power_level(1308, 1, 300))  # (227, 199, 19, 103)

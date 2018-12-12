import re

initial_state = "##.##.##..#..#.#.#.#...#...#####.###...#####.##..#####.#..#.##..#..#.#...#...##.##...#.##......####."

transitions = []

with open('../data/day12.txt', 'r') as data_file:
    for line in data_file:
        match = re.search('(?P<parent>(#|\.){5}) => (?P<child>#|\.)', line)
        transitions.append((match.group('parent'), match.group('child')))

print(transitions)

current_gen = '.....' + initial_state + '....'
next_gen = ''

FINAL_GEN = 120

sums = []

for j in range(FINAL_GEN):
    for i in range(len(current_gen)-4):
        for transition in transitions:
            if current_gen[i:i+5] == transition[0]:
                next_gen += transition[1]

    after_state = '..' + next_gen + '.'*(FINAL_GEN-j) + '..'
    print(after_state)

    current_gen = '..' + next_gen + '...'
    next_gen = ''
    sums.append(sum([m.start(0)-5 for m in re.finditer('#', after_state)]))

print(sums[19])
print([x-y for x, y in zip(sums[1:], sums[0:-1])])
print(sums[119] + 62 * (50000000000 - 120))

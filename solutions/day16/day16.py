import re
import unittest
from collections import defaultdict
from pprint import pprint
from typing import List, Set

import itertools


def addr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] + input_register[instruction[2]]
    return output_registers


def mulr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] * input_register[instruction[2]]
    return output_registers


def banr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] & input_register[instruction[2]]
    return output_registers


def borr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] | input_register[instruction[2]]
    return output_registers


def setr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]]
    return output_registers


def addi(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] + instruction[2]
    return output_registers


def muli(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] * instruction[2]
    return output_registers


def bani(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] & instruction[2]
    return output_registers


def bori(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = input_register[instruction[1]] | instruction[2]
    return output_registers


def seti(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    output_registers[instruction[3]] = instruction[1]
    return output_registers


def gtir(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if instruction[1] > input_register[instruction[2]]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


def gtri(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if input_register[instruction[1]] > instruction[2]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


def gtrr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if input_register[instruction[1]] > input_register[instruction[2]]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


def eqir(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if instruction[1] == input_register[instruction[2]]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


def eqri(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if input_register[instruction[1]] == instruction[2]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


def eqrr(input_register: List, instruction: tuple) -> List:
    output_registers = input_register.copy()
    if input_register[instruction[1]] == input_register[instruction[2]]:
        val = 1
    else:
        val = 0
    output_registers[instruction[3]] = val
    return output_registers


opcodes = (
    addr,
    mulr,
    banr,
    borr,
    setr,
    addi,
    muli,
    bani,
    bori,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
)


def opcodes_factory() -> Set:
    return itertools.repeat({opcode for opcode in opcodes}).__next__()


def match_opcodes_2(
        input_register: List[int],
        instructions: tuple,
        output_register: List[int]
) -> Set:
    matching_opcodes = set()
    for opcode in opcodes:
        if opcode(input_register, instructions) == output_register:
            matching_opcodes.add(opcode)
    return matching_opcodes


def match_opcodes(example: tuple) -> Set:
    return match_opcodes_2(example[0], example[1], example[2])


def extract_examples():
    examples = []
    with open("../../data/day16a.txt", "r") as file:
        match = re.match('Before: \[(\d+), (\d+), (\d+), (\d+)\]', file.readline())
        while match:
            input_register = [
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4))
            ]
            match = re.match('(\d+) (\d+) (\d+) (\d+)', file.readline())
            instructions = (
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4))
            )
            match = re.match('After: {2}\[(\d+), (\d+), (\d+), (\d+)\]', file.readline())
            output_register = [
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4))
            ]
            examples.append((
                input_register,
                instructions,
                output_register
            ))
            file.readline()  # skip empty line
            match = re.match('Before: \[(\d+), (\d+), (\d+), (\d+)\]', file.readline())

    return examples


def check_examples(examples):
    counts = defaultdict(int)
    potential_opcodes = defaultdict(lambda: opcodes_factory())
    for example in examples:
        matching_opcodes = match_opcodes(example)
        counts[len(matching_opcodes)] += 1
        potential_opcodes[example[1][0]] &= matching_opcodes
    return counts, potential_opcodes


def determine_codes(potential_opcodes):
    defined_codes = {}
    last_len = -1
    while last_len < len(defined_codes) < len(opcodes):
        last_len = len(defined_codes)
        defined_codes = {
            **defined_codes,
            **{
                code: functions.difference(defined_codes.values()).pop()
                for code, functions in potential_opcodes.items()
                if len(functions.difference(defined_codes.values())) == 1
            }
        }
    if len(defined_codes) != len(opcodes):
        print("not all opcodes where matched correctly, but no progress could be made anymore")
    return defined_codes


class TestDay16(unittest.TestCase):

    def test_addr(self):
        self.assertEqual(
            [3, 2, 4, 1],
            addr([3, 2, 2, 1], (9, 2, 1, 2))
        )

    def test_mulr(self):
        self.assertEqual(
            [3, 2, 2, 1],
            mulr([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_banr(self):
        self.assertEqual(
            [3, 2, 0, 1],
            banr([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_borr(self):
        self.assertEqual(
            [3, 2, 3, 1],
            borr([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_setr(self):
        self.assertEqual(
            [3, 2, 1, 1],
            setr([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_addi(self):
        self.assertEqual(
            [3, 2, 2, 1],
            addi([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_muli(self):
        self.assertEqual(
            [3, 2, 1, 1],
            muli([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_bani(self):
        self.assertEqual(
            [3, 2, 1, 1],
            bani([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_bori(self):
        self.assertEqual(
            [3, 2, 1, 1],
            bori([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_seti(self):
        self.assertEqual(
            [3, 2, 2, 1],
            seti([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_gtir(self):
        self.assertEqual(
            [3, 2, 0, 1],
            gtir([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_gtri(self):
        self.assertEqual(
            [3, 2, 0, 1],
            gtri([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_gtrr(self):
        self.assertEqual(
            [3, 2, 0, 1],
            gtrr([3, 2, 1, 1], (9, 2, 1, 2))
        )

    def test_count_possible_opcodes(self):
        self.assertEqual(
            {mulr, addi, seti},
            # 9 not MY input, just the example
            match_opcodes(([3, 2, 1, 1], (9, 2, 1, 2), [3, 2, 2, 1]))
        )

    def test_input_1_opcode_2_no_changes(self):
        self.assertEqual(
            {setr, gtir},
            match_opcodes(([1, 0, 2, 1], (2, 3, 2, 0), [1, 0, 2, 1]))
        )

    def test_input_opcode_2_with_change_first_case(self):
        self.assertEqual(
            {setr, gtir},
            match_opcodes(([2, 1, 2, 1], (2, 3, 2, 2), [2, 1, 1, 1]))
        )

    def test_input_opcode_2_with_change_third_case(self):
        self.assertEqual(
            {setr, gtir},
            match_opcodes(([0, 0, 2, 1], (2, 3, 2, 0), [1, 0, 2, 1]))
        )

    def test_input_opcode_3_with_only_one_match(self):
        self.assertEqual(
            {gtrr, eqir},
            # must be 1
            # - addr:2, addi:5, mulr:0, muli:6
            # - banr:0, bani:2, borr:2, bori:3
            # - setr:2, seti:0
            # - gtir:0, gtri:0, gtrr:0
            # - eqir:1, eqri:0, eqrr:0
            match_opcodes(([2, 2, 0, 0], (3, 0, 3, 0), [1, 2, 0, 0]))
        )

    def test_input_opcode_1_with_only_one_match(self):
        self.assertEqual(
            {gtri, eqir, eqrr},
            match_opcodes(([3, 2, 3, 3], (1, 3, 2, 2), [3, 2, 1, 3]))
        )

    def test_input_opcode_9_with_only_one_match(self):
        self.assertEqual(
            {gtrr},
            # must be 1
            # - addr:3, addi:5, mulr:2, muli:6
            # - banr:0, bani:2, borr:3, bori:3
            # - setr:2, seti:0, gtir:0, gtri:0, gtrr:1
            match_opcodes(([2, 2, 0, 1], (9, 0, 3, 0), [1, 2, 0, 1]))
        )

    def test_input(self):
        examples = extract_examples()
        print(len(examples))

        counts, potential_opcodes = check_examples(examples)

        print(counts)
        print(sum([cases for count, cases in counts.items() if count >= 3]))
        # pprint(potential_opcodes)

        # Part I:
        # 112 to low -- missed the equality operations
        # 165 to low -- 3 or more opcodes
        # 677

        defined_codes = determine_codes(potential_opcodes)

        print("defined codes:")
        pprint(defined_codes)

        print("not definable codes:")
        print({
            code: functions.difference(defined_codes.values())
            for code, functions in potential_opcodes.items()
        })

        register = [0, 0, 0, 0]

        with open("../../data/day16b.txt", "r") as file:

            match = re.match('(\d+) (\d+) (\d+) (\d+)', file.readline())
            while match:
                instructions = (
                    int(match.group(1)),
                    int(match.group(2)),
                    int(match.group(3)),
                    int(match.group(4))
                )

                register = defined_codes[instructions[0]](register, instructions)

                match = re.match('(\d+) (\d+) (\d+) (\d+)', file.readline())
            print(register)

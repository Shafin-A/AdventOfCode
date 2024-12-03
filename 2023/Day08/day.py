
import math


filename = "input.txt"


def parse_instructions_and_maps(filename):
    with open(filename) as file:
        instructions = file.readline()
        file.readline()
        maps = {}

        for line in file:
            [start, left_right_dest] = [x.strip() for x in line.split('=')]
            [left, right] = left_right_dest[1:-1].split(', ')
            maps[start] = [left, right]

        return instructions, maps


instructions, maps = parse_instructions_and_maps(filename)


def get_steps_p1(instructions, maps):
    current = 'AAA'
    steps = 0
    exit_flag = False

    while not exit_flag:
        for direction in instructions:
            if direction == 'R':
                current = maps[current][1]
                steps += 1

            elif direction == 'L':
                current = maps[current][0]
                steps += 1

            if current == 'ZZZ':
                exit_flag = True
                break

    return steps


def get_steps_p2(instructions, maps: dict[str, tuple]):
    starts = [x for x in maps.keys() if x.endswith('A')]
    steps = 0
    exit_flag = False

    while not exit_flag:
        for direction in instructions:
            if direction == 'R':
                for i, start in enumerate(starts):
                    starts[i] = maps[start][1]
                steps += 1

            elif direction == 'L':
                for i, start in enumerate(starts):
                    starts[i] = maps[start][0]
                steps += 1

            for start in starts:
                if not start.endswith('Z'):
                    exit_flag = False
                    break
                else:
                    exit_flag = True

    return steps


print(get_steps_p2(instructions, maps))

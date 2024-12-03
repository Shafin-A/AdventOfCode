import time

filename = "input.txt"


def parse_rocks(filename: str) -> list[str]:
    with open(filename) as file:
        rocks = []
        for line in file:
            rocks.append(line.strip())

        return rocks


def tilt(column: str, direction: int):
    column_list = list(column)
    did_swap = True

    while did_swap:
        did_swap = False

        if direction == 1:
            range_values = range(1, len(column_list))
        elif direction == -1:
            range_values = range(len(column_list) - 1, 0, -1)
        else:
            raise ValueError("Invalid direction.")

        for i in range_values:
            prev = column_list[i - 1]
            curr = column_list[i]

            if (direction == 1 and prev == '.' and curr == 'O') or (direction == -1 and prev == 'O' and curr == '.'):
                column_list[i], column_list[i -
                                            1] = column_list[i - 1], column_list[i]
                did_swap = True

    return ''.join(column_list)


def tilt_rocks_north(rocks: list[str]):
    tilted_rocks = [''] * len(rocks)

    for i in range(len(rocks[0])):
        column = ''
        for rock in rocks:
            column += rock[i]

        tilted_column = tilt(column, 1)

        for j, c in enumerate(tilted_column):
            tilted_rocks[j] += c

    return tilted_rocks


def tilt_rocks_west(rocks: list[str]) -> list[str]:
    tilted_rocks = []
    for rock in rocks:
        tilted_row = tilt(rock, 1)
        tilted_rocks.append(tilted_row)

    return tilted_rocks


def tilt_rocks_east(rocks: list[str]) -> list[str]:
    tilted_rocks = []
    for rock in rocks:
        tilted_row = tilt(rock, -1)
        tilted_rocks.append(tilted_row)

    return tilted_rocks


def tilt_rocks_south(rocks: list[str]):
    tilted_rocks = [''] * len(rocks)

    for i in range(len(rocks[0])):
        column = ''
        for rock in rocks:
            column += rock[i]

        tilted_column = tilt(column, -1)

        for j, c in enumerate(tilted_column):
            tilted_rocks[j] += c

    return tilted_rocks


def cycle(rocks: list[str]):

    north_tilted_rocks = tilt_rocks_north(rocks)
    west_tilted_rocks = tilt_rocks_west(north_tilted_rocks)
    south_tilted_rocks = tilt_rocks_south(west_tilted_rocks)
    east_tilted_rocks = tilt_rocks_east(south_tilted_rocks)

    return east_tilted_rocks


def run_cycle(rocks: list[str], num_times: int):
    seen_states = set()

    for i in range(num_times):
        cycled_rocks = cycle(rocks)
        state = tuple(cycled_rocks)

        if state in seen_states:
            print(f"Match found at iteration {i}.")
            break

        seen_states.add(state)
        rocks = cycled_rocks

    return rocks


rocks = parse_rocks(filename)


def part_1(rocks):
    rocks = tilt_rocks_north(rocks)
    loads = [(len(rocks) - i) * rock.count('O')
             for i, rock in enumerate(rocks)]

    return sum(loads)


def part_2(rocks):
    rocks = run_cycle(rocks, 1000000000)
    loads = [(len(rocks) - i) * rock.count('O')
             for i, rock in enumerate(rocks)]

    return sum(loads)


start = time.time()
print(part_1(rocks))
end = time.time()
print(f"{end - start} seconds")

start = time.time()
print(part_2(rocks))
end = time.time()
print(f"{end - start} seconds")

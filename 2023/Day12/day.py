import functools
from itertools import product

filename = "input.txt"


def parse_input(filename):
    with open(filename) as file:
        rows = []
        for line in file:
            row, condition_str = line.split()
            condition = [int(i) for i in condition_str.split(',')]

            new_row = ''
            new_condition = []
            for _ in range(5):
                new_row += row + '?'
                new_condition.extend(condition)

            rows.append((new_row[:-1], new_condition))
        return rows


def is_valid_row(row: str, condition: list[int]):
    splitted = row.split('.')
    splitted = [x for x in splitted if x]

    if len(splitted) != len(condition):
        return False

    for i, s in enumerate(splitted):
        if len(s) != condition[i]:
            return False

    return True


@functools.lru_cache(maxsize=None)
def generate_combinations(s):
    replacements = ('.', '#')
    all_combinations = []

    for combination in product(replacements, repeat=s.count('?')):
        new_string = s.replace('?', '{}').format(*combination)
        all_combinations.append(new_string)

    return all_combinations


rows = parse_input(filename)

valids = []
for row, condition in rows:
    combinations = generate_combinations(row)
    count = 0

    for combination in combinations:
        if is_valid_row(combination, condition):
            count += 1

    valids.append(count)

print(sum(valids))

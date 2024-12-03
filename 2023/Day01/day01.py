
filename = 'day01_input.txt'


def get_first_last_num_part_1(s: str):
    first_num = -1
    last_num = -1

    for c in s:
        if c.isdigit():
            if first_num == -1:
                first_num = int(c)
            last_num = int(c)

    return first_num * 10 + last_num


def sum_calibration_values_part_1(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            sum += get_first_last_num_part_1(line)

    return sum


number_mapping = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}


def get_first_last_num_part_2(s: str):
    first_num = -1
    last_num = -1

    new_s = s
    for word in number_mapping:
        new_s = new_s.replace(word, number_mapping[word])

    for c in new_s:
        if c.isdigit():
            if first_num == -1:
                first_num = int(c)
            last_num = int(c)

    return first_num * 10 + last_num


def sum_calibration_values_part_2(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            sum += get_first_last_num_part_2(line)

    return sum


print(sum_calibration_values_part_1(filename=filename))
print(sum_calibration_values_part_2(filename=filename))

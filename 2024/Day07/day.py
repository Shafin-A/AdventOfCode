def parse_input(filename: str) -> dict[int, list[int]]:
    calibration_values = {}

    with open(filename) as file:
        for line in file:

            target, values = line.split(':')
            target = int(target)
            values = [int(i) for i in values.strip().split(" ")]
            calibration_values[target] = values

    return calibration_values


def can_create_number(target: int, numbers: list[int], current: int, do_concat: bool) -> bool:
    if current > target:
        return False
    if not numbers:
        return current == target

    next_number = numbers[0]
    remaining_numbers = numbers[1:]

    if can_create_number(target, remaining_numbers, current + next_number, do_concat):
        return True

    if can_create_number(target, remaining_numbers, current * next_number, do_concat):
        return True

    if do_concat:
        if can_create_number(target, remaining_numbers, int(str(current) + str(next_number)), do_concat):
            return True

    return False


def calculate_total_calibration(calibration_values: dict[int, list[int]], do_concat: bool) -> int:
    total = 0

    for target, numbers in calibration_values.items():
        if can_create_number(target, numbers, 0, do_concat):
            total += target

    return total


if __name__ == "__main__":
    filename = "input.txt"

    calibration_values = parse_input(filename)

    print(calculate_total_calibration(calibration_values, False))
    print(calculate_total_calibration(calibration_values, True))

def read_input(filename: str) -> list[list[int]]:
    all_levels = []
    with open(filename) as file:
        for line in file:
            levels = [int(i) for i in line.split(" ")]
            all_levels.append(levels)
    return all_levels


def is_all_increasing(arr: list[int]):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True


def is_all_decreasing(arr: list[int]):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return False
    return True


def are_levels_unsafe(levels: list[int]):
    is_unsafe = True

    if is_all_increasing(levels) or is_all_decreasing(levels):
        is_unsafe = False

        for i in range(1, len(levels)):
            if not is_unsafe:
                diff = abs(levels[i] - levels[i - 1])
                if not 1 <= diff <= 3:
                    is_unsafe = True

    return is_unsafe


def num_safe_reports(all_levels: list[list[int]]):
    num_safe = 0

    for levels in all_levels:
        is_unsafe = are_levels_unsafe(levels)

        if not is_unsafe:
            num_safe += 1

    return num_safe


def num_safe_reports_dampener(all_levels: list[list[int]]):
    num_safe = 0

    for levels in all_levels:
        is_unsafe = are_levels_unsafe(levels)

        if not is_unsafe:
            num_safe += 1

        else:
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i+1:]

                if not are_levels_unsafe(modified_levels):
                    num_safe += 1
                    break

    return num_safe


if __name__ == "__main__":
    filename = "input.txt"
    all_levels = read_input(filename)

    print(num_safe_reports(all_levels))
    print(num_safe_reports_dampener(all_levels))

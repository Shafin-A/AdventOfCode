from collections import defaultdict


def parse_input(filename: str):
    order_rules: defaultdict[int, set[int]] = defaultdict(set[int])
    page_numbers: list[list[int]] = []

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            if line:
                if "|" in line:
                    order = line.split("|")
                    order_rules[int(order[1])].add(int(order[0]))

                else:
                    numbers = line.split(",")
                    numbers = [int(i) for i in numbers]
                    page_numbers.append(numbers)

    return order_rules, page_numbers


def calculate_correct_orders(order_rules: defaultdict[int, set[int]], page_numbers: list[list[int]]):
    num_correct_orders = 0

    for numbers in page_numbers:
        is_correct = True

        for i, number in enumerate(numbers):
            if number in order_rules:
                required_pages = order_rules[number]

                rest_numbers = numbers[i+1:]

                for page in required_pages:
                    if page in rest_numbers:
                        is_correct = False
                        break

                if not is_correct:
                    break

        if is_correct:
            mid_number = numbers[len(numbers) // 2]
            num_correct_orders += mid_number

    return num_correct_orders


def get_incorrect_numbers(numbers):
    incorrect_numbers: list[list[int]] = []

    for numbers in page_numbers:
        is_correct = True

        for i, number in enumerate(numbers):
            if number in order_rules:
                required_pages = order_rules[number]

                rest_numbers = set(numbers[i+1:])

                for page in required_pages:
                    if page in rest_numbers:
                        is_correct = False
                        incorrect_numbers.append(numbers)
                        break

                if not is_correct:
                    break

    return incorrect_numbers


def calculate_corrected_incorrect_orders(order_rules: defaultdict[int, set[int]], page_numbers: list[list[int]]):
    num_corrected_orders = 0

    incorrect_numbers = get_incorrect_numbers(page_numbers)

    all_corrected = False
    while not all_corrected:
        for numbers in incorrect_numbers:
            for i in range(len(numbers)):
                number = numbers[i]
                if number in order_rules:
                    required_pages = order_rules[number]

                    rest_numbers = set(numbers[i+1:])

                    for page in required_pages:
                        if page in rest_numbers:
                            j = numbers.index(page)
                            numbers[i], numbers[j] = numbers[j], numbers[i]

        all_corrected = len(get_incorrect_numbers(incorrect_numbers)) == 0

    for numbers in incorrect_numbers:
        mid_number = numbers[len(numbers) // 2]
        num_corrected_orders += mid_number

    return num_corrected_orders


if __name__ == "__main__":
    filename = "input.txt"

    order_rules, page_numbers = parse_input(filename)

    print(calculate_correct_orders(order_rules, page_numbers))
    print(calculate_corrected_incorrect_orders(order_rules, page_numbers))

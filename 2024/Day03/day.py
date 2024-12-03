import re


def parse_input(filename: str) -> list[str]:
    instructions = []

    with open(filename) as file:
        for line in file:
            instructions.append(line)

    return instructions


def calculate_instructions_sum(instructions: list[str]) -> int:
    mul_sum = 0

    for instruction in instructions:
        muls = re.findall(r"mul\(\d*,\d*\)", instruction)
        for mul in muls:
            nums = re.findall(r'\d+', mul)

            nums_mul = int(nums[0]) * int(nums[1])

            mul_sum += nums_mul

    return mul_sum


def calculate_instructions_sum_conditional(instructions: list[str]) -> int:
    mul_sum = 0
    do_mul = True

    for instruction in instructions:
        muls: list[str] = re.findall(
            r"(mul\(\d*,\d*\)|do\(\)|don't\(\))", instruction)

        for mul in muls:
            if mul.startswith("mul") and do_mul:
                nums = re.findall(r'\d+', mul)

                nums_mul = int(nums[0]) * int(nums[1])

                mul_sum += nums_mul

            elif mul == "do()":
                do_mul = True
            else:
                do_mul = False

    return mul_sum


if __name__ == "__main__":
    filename = "input.txt"

    instructions = parse_input(filename)

    print(calculate_instructions_sum(instructions))
    print(calculate_instructions_sum_conditional(instructions))

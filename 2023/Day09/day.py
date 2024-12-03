filename = "input.txt"


def parse_nums(filename) -> list[list[int]]:
    with open(filename) as file:
        all_nums = []

        for line in file:
            nums = [int(i) for i in line.strip().split()]
            all_nums.append(nums)

        return all_nums


def get_predicted_value(nums: list[int]) -> int:

    all_differences = [nums]

    while True:
        current_nums = all_differences[-1]
        differences = []

        for i in range(len(current_nums)):
            num = current_nums[i]
            next_num = current_nums[i+1] if i+1 < len(current_nums) else None

            if next_num is None:
                break

            differences.append(next_num - num)

        all_differences.append(differences)

        if differences[0] == 0 and len(set(differences)) == 1:
            break

    return sum(i[-1] for i in all_differences)


all_nums = parse_nums(filename)

p1 = sum(get_predicted_value(nums) for nums in all_nums)
p2 = sum(get_predicted_value(nums[::-1]) for nums in all_nums)

print(p1)
print(p2)

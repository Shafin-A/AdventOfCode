from collections import Counter


def read_input(filename):
    list1, list2 = [], []
    with open(filename) as file:
        for line in file:
            num1, num2 = line.split()
            num1, num2 = int(num1), int(num2)

            list1.append(num1)
            list2.append(num2)

    return sorted(list1), sorted(list2)


def calculate_sum_result(list1, list2):
    sum_result = 0

    for i in range(len(list1)):
        sum_result += abs(list1[i] - list2[i])

    return sum_result


def calculate_sim_result(list1, list2):
    counts = Counter(list2)
    sim_result = 0

    for i in range(len(list1)):
        sim_result += list1[i] * counts[list1[i]]

    return sim_result


if __name__ == "__main__":
    filename = "input.txt"

    list1, list2 = read_input(filename)

    sum_result = calculate_sum_result(list1, list2)
    print(sum_result)

    sim_result = calculate_sim_result(list1, list2)
    print(sim_result)

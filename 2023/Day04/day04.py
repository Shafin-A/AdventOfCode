filename = 'day04_input.txt'


def get_scratch_card_worth(line: str):
    [_, numbers] = line.split(':')

    [winning_nums, hand] = numbers.split('|')

    winning_nums = winning_nums.strip().split()
    hand = hand.strip().split()

    num_intersections = len(set(winning_nums).intersection(hand))

    if (num_intersections <= 1):
        return num_intersections

    return 2**(num_intersections-1)


def get_scratch_cards_worth(filename):
    sum = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            sum += get_scratch_card_worth(line)

    return sum


def get_scratch_cards_worth_part_2(filename):

    with open(filename) as file:
        cards = file.readlines()

        results = [1] * len(cards)

        i = 0

        while True:
            if (i >= len(cards)):
                break

            card = cards[i]

            [_, numbers] = card.split(':')

            [winning_nums, hand] = numbers.split('|')

            winning_nums = winning_nums.strip().split()
            hand = hand.strip().split()

            num_intersections = len(set(winning_nums).intersection(hand))

            for j in range(num_intersections):
                results[i+j+1] += results[i]

            i += 1

    return sum(results)


print(get_scratch_cards_worth_part_2(filename))

from collections import Counter

import functools
from typing import Self


filename = "input.txt"


@functools.total_ordering
class Card:
    ALLOWED_LABELS = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10,
                      '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def __init__(self, label):
        if str(label) not in self.ALLOWED_LABELS:
            raise ValueError(
                f"Invalid label. Allowed labels are: {', '.join(self.ALLOWED_LABELS.keys())}")
        self.label = str(label)

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        return self.ALLOWED_LABELS[self.label] < self.ALLOWED_LABELS[other.label]


def get_hand_type(cards: list[Card]):

    card_counts = Counter([card.label for card in cards])
    most_common = card_counts.most_common()

    (greatest_card, greatest_count) = most_common[0]

    if (greatest_card == 'J' and greatest_count == 5):  # JJJJJ case
        return 6

    if greatest_card == 'J':  # make greatest card second most greatest after J
        (greatest_card, _) = most_common[1]

    if 'J' in card_counts:  # add J counts to greatest card and remove J
        card_counts[greatest_card] += card_counts.pop('J')

    if 5 in card_counts.values():
        return 6
    elif 4 in card_counts.values():
        return 5
    elif sorted(card_counts.values()) == [2, 3]:
        return 4
    elif 3 in card_counts.values():
        return 3
    elif sorted(card_counts.values()) == [1, 2, 2]:
        return 2
    elif 2 in card_counts.values():
        return 1
    else:
        return 0


@functools.total_ordering
class Hand:
    def __init__(self, cards: list[Card]):
        if (len(cards) != 5):
            raise ValueError(
                f"Hands should have 5 Cards. Got {len(cards)} cards")
        self.cards = cards
        self.hand_type = get_hand_type(cards)

    def __str__(self):
        return f"Cards={self.cards}, Type={self.hand_type}"

    def __repr__(self):
        return f"Cards={self.cards}, Type={self.hand_type}"

    def __eq__(self, other):
        if self.hand_type != other.hand_type:
            return False

        for card1, card2 in zip(self.cards, other.cards):
            if card1 != card2:
                return False

        return True

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False

        for card1, card2 in zip(self.cards, other.cards):
            if card1 < card2:
                return True
            elif card1 > card2:
                return False

        return False

    def __hash__(self):
        return hash(repr(self))


def parse_hands_and_bids(filename):

    hands_and_bids: dict[Hand, int] = {}

    with open(filename) as file:
        for line in file:
            [hand, bid] = line.split()

            cards = [Card(card) for card in hand]
            hands_and_bids[Hand(cards)] = int(bid)

    return hands_and_bids


hands_and_bids = parse_hands_and_bids(filename)

hands = hands_and_bids.keys()

sorted_hands = sorted(hands)

winnings = []
for rank, hand in enumerate(sorted_hands, start=1):
    winning = rank * hands_and_bids[hand]
    winnings.append(winning)

print(sum(winnings))

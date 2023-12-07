import collections
import functools
from typing import TextIO

CARD_VALUE = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'j': 1
}


def parse_input(file: TextIO):
    hand_to_bid = {}

    for line in file:
        split_line = line.split()
        hand_to_bid[split_line[0]] = int(split_line[1])

    return hand_to_bid


def compare_cards(card1, card2):
    if CARD_VALUE[card1] > CARD_VALUE[card2]:
        return 1
    if CARD_VALUE[card1] == CARD_VALUE[card2]:
        return 0
    if CARD_VALUE[card1] < CARD_VALUE[card2]:
        return -1


def compare_card_counts(count1: list[int], count2: list[int]):
    if len(count1) == len(count2):
        if count1[-1] > count2[-1]:
            return 1
        if count1[-1] == count2[-1]:
            return 0
        if count1[-1] < count2[-1]:
            return -1
    return len(count2) - len(count1)


def compare_hand_cards(c1, c2):
    for i in range(len(c1)):
        comp_val = compare_cards(c1[i], c2[i])
        if comp_val != 0:
            return comp_val

    return 0


def calc_hand_value(hands: list[str], is_joker=False):
    hand_to_values = {}

    for hand in hands:

        counted_cards = dict(collections.Counter(list(hand)).most_common())

        if is_joker and 'j' in counted_cards and counted_cards['j'] < 5:
            val = counted_cards.pop('j')
            topmost_key = list(counted_cards.keys())[0]
            counted_cards[topmost_key] = counted_cards[topmost_key] + val

        values = sorted(counted_cards.values())
        hand_to_values[hand] = values

    return hand_to_values


def sort_cards(row1, row2):
    card1, values1 = row1
    card2, values2 = row2

    compared = compare_card_counts(values1, values2)

    if compared == 0:
        return compare_hand_cards(card1, card2)

    return compared


def get_hand_rank(hand_to_value: dict[str, list[int]]):
    return sorted(hand_to_value.items(), key=functools.cmp_to_key(sort_cards))


def p1(input: dict[str, int]) -> int:
    input = normalize_input(input)
    hand_values = calc_hand_value(list(input.keys()))
    hand_ranks = get_hand_rank(hand_values)

    sums = []
    for idx, val in enumerate(hand_ranks):
        sums.append(input[val[0]] * (idx + 1))

    return sum(sums)


def p2(input) -> int:
    input = normalize_input(input, True)
    hand_values = calc_hand_value(list(input.keys()), is_joker=True)
    hand_ranks = get_hand_rank(hand_values)

    sums = []
    for idx, val in enumerate(hand_ranks):
        sums.append(input[val[0]] * (idx + 1))

    return sum(sums)


def normalize_input(raw_input, is_joker=False):
    normalized = {}

    for (hand, val) in raw_input.items():
        normalized_hand = hand.replace("J", 'j') if is_joker else hand

        normalized[normalized_hand] = val

    return normalized


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print('p1', p1(parsed_input))
        print('p2', p2(parsed_input))


if __name__ == '__main__':
    run()

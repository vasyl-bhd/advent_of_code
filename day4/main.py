import math
from typing import TextIO


def parse_input(file: TextIO) -> dict[int, dict[str, list[int]]]:
    lines = [line.rstrip() for line in file]
    parsed_input = {}
    for line in lines:
        card_to_all_numbers = line.split(":")
        card_id = int(card_to_all_numbers[0].split()[1])
        all_numbers = card_to_all_numbers[1].split(" | ")
        winning_numbers = [int(num) for num in all_numbers[0].split()]
        my_numbers = [int(num) for num in all_numbers[1].split()]

        parsed_input[card_id] = {
            'w': winning_numbers,
            'm': my_numbers
        }
    return parsed_input


def card_id_to_matching_numbers(inpt: dict[int, dict[str, list[int]]]):
    card_id_to_match = {}
    for key, numbers in inpt.items():
        winning = numbers['w']
        my = numbers['m']

        same_numbers_count = len([n for n in my if n in winning])

        card_id_to_match[key] = same_numbers_count

    return card_id_to_match


def p1(inpt: dict[int, int]) -> dict[int, int]:
    card_id_to_winning_count = {}
    for key, same_numbers_count in inpt.items():
        winning_prod = pow(2, same_numbers_count - 1)

        card_id_to_winning_count[key] = math.floor(winning_prod)

    return card_id_to_winning_count


def p2(inpt: dict[int, int]) -> list[int]:
    card_with_copies_list = list(inpt.keys())
    i = 0

    while i < len(card_with_copies_list):
        card_id = card_with_copies_list[i]
        matched_num_count = inpt[card_id]

        original_card_copies = [card for card in range(card_id + 1, card_id + matched_num_count + 1)]

        card_with_copies_list.extend(original_card_copies)

        i += 1

    return sorted(card_with_copies_list)


def run():
    with open("input.txt") as file:
        inpt = parse_input(file)
        card_to_matching_numbers = card_id_to_matching_numbers(inpt)

        print(len(p2(card_to_matching_numbers)))


run()

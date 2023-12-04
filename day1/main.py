import re
from typing import TextIO


def parse_input(file: TextIO) -> list[str]:
    inputs = [line.rstrip() for line in file]

    return [word for word in inputs]


def p1(words: list[str]):
    nums = []
    for word in words:
        x = re.findall('([0-9])(?:.*([0-9]))?', word)[0]
        num = ''

        if (x[1] != ''):
            num = x[0] + x[1]
        else:
            num = x[0] + x[0]

        nums.append(int(num))

    return sum(nums)


def p2(words: list[str]):
    nums = []
    word_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for word in words:
        x = re.findall(
            '(one|two|three|four|five|six|seven|eight|nine|[0-9])(?:.*(one|two|three|four|five|six|seven|eight|nine|[0-9]))?',
            word)[0]
        first_char = word_to_num[x[0]] if (x[0] in word_to_num) else x[0]
        second_char = word_to_num[x[1]] if (x[1] in word_to_num) else x[1]
        print(first_char, second_char)
        num = first_char + second_char

        nums.append(int(num))

    return sum(nums)


def run():
    with open("input.txt") as file:
        input = parse_input(file)
        print(p1(input))
        print(p2(input))


run()

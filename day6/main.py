import math
from typing import TextIO


def parse_input(file: TextIO):
    parsed_input = {}

    for line in file:
        row = line.split(": ")
        parsed_input[row[0].strip().lower()] = [int(val) for val in row[1].strip().split()]

    return parsed_input


def get_acceptable_ways_to_hold(single_input: [int, int]):
    round_time = single_input[0]
    record_distance = single_input[1]

    # x - acceptable hold time range
    # T - round time
    # L - record
    # (T - x) * x > L
    # xT - x*x - L > 0
    # -x*x + Round_time*x - record_distance = 0

    d = round_time * round_time - 4 * record_distance

    x1 = int((round_time + d ** 0.5) / 2)
    x2 = int((round_time - d ** 0.5) / 2)

    # hack from SO
    return x1 - x2 - (d == math.isqrt(d) ** 2)


def p1(input: dict[str, list[int]]) -> int:
    formatted_input = []
    for i in range(0, len(input['time'])):
        formatted_input.append((input['time'][i], input['distance'][i]))

    acceptable_hold_time = [get_acceptable_ways_to_hold(round) for round in formatted_input]

    return math.prod(acceptable_hold_time)


def p2(input: dict[str, list[int]]) -> int:
    round_time = int(''.join([str(x) for x in input['time']]))
    round_distance = int(''.join([str(x) for x in input['distance']]))

    return get_acceptable_ways_to_hold((round_time, round_distance))


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print(p1(parsed_input))
        print(p2(parsed_input))


if __name__ == '__main__':
    run()

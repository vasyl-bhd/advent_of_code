import math
from typing import TextIO

GLOBAL_MAXES = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse_input(file: TextIO) -> dict[str, list[dict[str, int]]]:
    inputs = [line.rstrip() for line in file]

    games_to_picks = {}

    for input in inputs:
        game_to_picks_arr = input.split(":")
        game_id = game_to_picks_arr[0].split()[1]
        pick_strings = game_to_picks_arr[1].split(";")

        rounds = []
        for string in pick_strings:
            color_picks = {}
            colors = string.split(", ")
            for color in colors:
                c = color.split()
                color_picks[c[1]] = int(c[0])
            rounds.append(color_picks)

        games_to_picks[game_id] = rounds

    return games_to_picks


def p1(games: dict[str, list[dict[str, str]]]):
    possible_game_ids = []

    for (game_id, rounds) in games.items():
        maxes_for_game: dict[str, int] = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for round in rounds:
            for (color, maxes) in round.items():
                maxes_for_game[color] = max(maxes_for_game[color], round[color])

        if (maxes_for_game['red'] <= GLOBAL_MAXES['red']
                and maxes_for_game['blue'] <= GLOBAL_MAXES['blue']
                and maxes_for_game['green'] <= GLOBAL_MAXES['green']):
            possible_game_ids.append(int(game_id))

    return sum(possible_game_ids)


def p2(games: dict[str, list[dict[str, str]]]):
    total_prod = 0
    for (game_id, rounds) in games.items():
        maxes_for_game: dict[str, int] = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for round in rounds:
            for (color, maxes) in round.items():
                maxes_for_game[color] = max(maxes_for_game[color], round[color])

        total_prod += math.prod(maxes_for_game.values())

    return total_prod




def run():
    with open("input.txt") as file:
        input = parse_input(file)
        print(input)
        print(p2(input))


run()

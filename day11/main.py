from itertools import combinations
from typing import TextIO


def parse_input(file: TextIO):
    return [line.strip() for line in file]


def get_galaxy_coords_after_expansion(galaxy: list[str], coords: tuple[int, int], exp_factor: int):
    empty_rows = [y for y, row in enumerate(galaxy)
                  if all(char == '.' for char in row)]
    empty_cols = [x for x, cols in enumerate(zip(*galaxy))
                  if all(char == '.' for char in cols)]

    empty_cols_before = sum([1 for col in empty_cols if col < coords[0]])
    empty_rows_before = sum([1 for row in empty_rows if row < coords[1]])

    return (coords[0] + empty_cols_before * (exp_factor - 1),
            coords[1] + empty_rows_before * (exp_factor - 1))


# Thanks SO, goddamit
def get_manhattan_distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def get_shortest_paths_between_galaxies(input: list[str], exp_factor: int):
    galaxies = []
    for r_idx, row in enumerate(input):
        for c_idx, char in enumerate(row):
            if char == '#':
                g_x, g_y = get_galaxy_coords_after_expansion(input, (c_idx, r_idx), exp_factor)
                galaxies.append((g_x, g_y))

    return [get_manhattan_distance(g1, g2) for g1, g2 in combinations(galaxies, 2)]


def p1(input):
    shortest_dist = get_shortest_paths_between_galaxies(input, 2)

    return sum(shortest_dist)


def p2(input):
    shortest_dist = get_shortest_paths_between_galaxies(input, 1_000_000)

    return sum(shortest_dist)


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print('p1', p1(parsed_input))
        print('p2', p2(parsed_input))


if __name__ == '__main__':
    run()

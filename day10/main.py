import sys
from collections import defaultdict, deque
from typing import TextIO

index_map = {
    '|': ([-1, 0], [1, 0]),
    '-': ([0, -1], [0, 1]),
    "L": ([-1, 0], [0, 1]),
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def parse_input(file: TextIO):
    pipes = []
    for line in file:
        pipes.extend(line.split())

    return pipes


def get_adjacent_map(input):
    adjacents = defaultdict(list)

    start_coords = None
    for r_idx, row in enumerate(input):
        for c_idx, column in enumerate(row):
            if column == 'S':
                start_coords = (r_idx, c_idx)
            if column in index_map:
                curr_symbol = index_map[column]
                adjacent = [(r_idx + curr_symbol[0][0], c_idx + curr_symbol[0][1]),
                            (r_idx + curr_symbol[1][0], c_idx + curr_symbol[1][1])]

                for x, y in adjacent:
                    if 0 <= x < len(input) and 0 <= y < len(row):
                        adjacents[(r_idx, c_idx)].append((x, y))

    starting_neighbours = []
    for adj in adjacents:
        for vert in adjacents[adj]:
            if vert == start_coords:
                starting_neighbours.append(adj)
                break

    adjacents[start_coords] = starting_neighbours

    return adjacents, start_coords


def bfs_stuff(adj_map, start):
    max_size = sys.maxsize
    distances = defaultdict(lambda: max_size)
    
    visited = deque()
    visited.append(start)
    
    distances[start] = 0
    
    answer = (0, start)
    
    while len(visited) > 0:
        curr_el = visited.popleft()
        for coords in adj_map[curr_el]:
            if distances[coords] == max_size:
                distances[coords] = distances[curr_el] + 1
                answer = max(answer, (distances[coords], coords))
                visited.append(coords)
    return answer

def p1(input):
    adj_map, start = get_adjacent_map(input)
    answ = bfs_stuff(adj_map, start)

    return answ[0]




def p2(input):
    # done manually =(
    pass


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print('p1', p1(parsed_input))
        print('p2', p2(parsed_input))


if __name__ == '__main__':
    run()

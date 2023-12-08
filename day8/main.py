import itertools
import math
from typing import TextIO


def parse_input(file: TextIO):
    split_input = file.read().split("\n")
    instructions = list(map(lambda x: 0 if x == 'L' else 1, list(split_input[0])))
    paths_arr = split_input[2:]

    kinda_graph = {}
    for path in paths_arr:
        path_to_nodes = path.split(" = ")

        nodes = path_to_nodes[1].split(", ")
        kinda_graph[path_to_nodes[0]] = (nodes[0].removeprefix("("), nodes[1].removesuffix(")"))

    return instructions, kinda_graph


def p1(input):
    instructions, data = input

    inst_cycle = itertools.cycle(instructions)
    curr, end = 'AAA', 'ZZZ'

    num_steps = 0

    for i in inst_cycle:
        if curr == end:
            break

        curr = data[curr][i]
        num_steps += 1

    return num_steps


def p2(input):
    instructions, data = input

    start_list = [node for node in data.keys() if node.endswith('A')]

    num_steps = set()

    for node in start_list:
        curr_node = node
        steps_for_node = 0

        for i in itertools.cycle(instructions):
            if curr_node.endswith('Z'):
                num_steps.add(steps_for_node)
                break

            curr_node = data[curr_node][i]
            steps_for_node += 1

    return math.lcm(*num_steps)


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print('p1', p1(parsed_input))
        print('p2', p2(parsed_input))


if __name__ == '__main__':
    run()

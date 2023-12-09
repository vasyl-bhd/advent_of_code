from typing import TextIO


def parse_input(file: TextIO):
    seqs = []

    for line in file:
        seqs.append([int(num) for num in line.split()])

    return seqs


def get_interpolated_seqs(sequence: list[int], find_last=True):
    interpolated_seqs = [sequence]

    while True:
        last_item = interpolated_seqs[-1]
        all_in_seq_zero = all([num == 0 for num in last_item])

        if all_in_seq_zero:
            break

        interpolated = []
        for i in range(len(last_item) - 1, 0, -1):
            first_item = last_item[i - 1] if find_last else last_item[i]
            second_item = last_item[i] if find_last else last_item[i - 1]

            interpolated.append(second_item - first_item)

        interpolated_seqs.append(list(reversed(interpolated)))

    index_to_find = -1 if find_last else 0
    last_values = map(lambda x: x[index_to_find], interpolated_seqs)

    return sum(last_values)


def p1(input):
    iterpolated_vals = []

    for sequence in input:
        iterpolated_vals.append(get_interpolated_seqs(sequence, True))

    return sum(iterpolated_vals)


def p2(input):
    iterpolated_vals = []
    for sequence in input:
        iterpolated_vals.append(get_interpolated_seqs(sequence, False))

    return sum(iterpolated_vals)


def run():
    with open('input.txt') as file:
        parsed_input = parse_input(file)
        print('p1', p1(parsed_input))
        print('p2', p2(parsed_input))


if __name__ == '__main__':
    run()

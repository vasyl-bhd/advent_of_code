from typing import TextIO, List, Tuple


def parse_input(file: TextIO):
    lines = file.read()
    seed, *maps = lines.split("\n\n")

    seeds = [int(seed) for seed in seed.split(": ")[1].split()]

    map_to_mappings = {}
    for map in maps:
        name_to_values = map.split(":")
        map_name = name_to_values[0].split()[0]
        space, *map_vals = name_to_values[1].split("\n")
        map_to_mappings[map_name] = [tuple([int(v) for v in val.split()]) for val in map_vals]

    return seeds, map_to_mappings


def get_mapping_ranges(maps_vals: list[tuple[int, int, int]]):
    ranges = []
    for val in maps_vals:
        source = val[1]
        destination = val[0]
        dist = val[2]

        destination_range = range(destination, destination + dist)
        source_range = range(source, source + dist)

        ranges.extend([(source_range, destination_range)])

    return ranges


def get_location_for_seed(seed: str, map_to_ranges: list[tuple[str, list[tuple[range, range]]]]):
    loc = seed
    for (name, ranges) in map_to_ranges:
        for rngs in ranges:
            source_range = rngs[0]
            dest_range = rngs[1]
            if loc in source_range:
                loc = dest_range[source_range.index(loc)]
                break

    return loc


def parse_seeds_pair(seeds: list[str]) -> list[range]:
    seed_it = iter(seeds)
    kek = list(zip(seed_it, seed_it))

    seeds = []

    for rng in kek:
        seeds.append(range(rng[0], rng[0] + rng[1]))

    return seeds


def p1(inpt: (list[str], dict[str, list[tuple[str, str, str]]])):
    map_to_ranges = [(name, get_mapping_ranges(mappings)) for name, mappings in inpt[1].items()]
    return min([get_location_for_seed(s, map_to_ranges) for s in inpt[0]])


def p2(inpt: (list[str], dict[str, list[tuple[str, str, str]]])):
    actual_seeds = parse_seeds_pair(inpt[0])
    map_to_ranges = [(name, get_mapping_ranges(mappings)) for name, mappings in inpt[1].items()]

    return min([get_location_for_seed(item, map_to_ranges) for rng in actual_seeds for item in rng])


def run():
    with open('input.txt') as file:
        inpt = parse_input(file)
        print(p1(inpt))

        print(p2(inpt))


if __name__ == '__main__':
    run()

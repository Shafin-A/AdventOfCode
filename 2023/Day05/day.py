filename = 'input.txt'


def get_maps_from_input(filename):
    with open(filename, 'r') as file:
        seeds_line = file.readline()

        seeds = [int(n) for n in seeds_line.split(':')[1].split()]

        maps = {'seed-to-soil': [], 'soil-to-fertilizer': [], 'fertilizer-to-water': [],
                'water-to-light': [], 'light-to-temperature': [], 'temperature-to-humidity': [],
                'humidity-to-location': []}

        current_map = None

        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue

            if line.endswith('map:'):
                current_map = maps[line[:-5]]
            elif current_map is not None:
                current_map.append([int(n) for n in line.split()])

        return seeds, maps


seeds, maps = get_maps_from_input(filename)


def compute_location(seed):
    current_value = seed

    for mapping in maps['seed-to-soil']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['soil-to-fertilizer']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['fertilizer-to-water']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['water-to-light']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['light-to-temperature']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['temperature-to-humidity']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    for mapping in maps['humidity-to-location']:
        dest, src, rng = mapping
        if src <= current_value < src + rng:
            current_value = dest + (current_value - src)
            break

    return current_value


min_location = float('inf')

total_seeds = len(seeds)
for outer_idx in range(0, len(seeds), 2):

    seed_start = seeds[outer_idx]
    seed_end = seeds[outer_idx+1]

    for inner_idx, seed in enumerate(range(seed_start, seed_start + seed_end)):

        location = compute_location(seed)
        if location < min_location:
            min_location = location

        # Print progress for both outer and inner loops
        outer_progress = (outer_idx + inner_idx / seed_end) / total_seeds * 100
        inner_progress = inner_idx / seed_end * 100
        print(
            f"Outer Progress: {outer_progress:.2f}%, Inner Progress: {inner_progress:.2f}%", end="\r")
print()
print(min_location)

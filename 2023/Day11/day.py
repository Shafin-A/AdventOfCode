import itertools

filename = "input.txt"


def parse_galaxies_image(filename: str):
    with open(filename) as file:
        image: list[list[str]] = []
        galaxies: list[tuple[int, int]] = []
        empty_row_indices: list[int] = []
        empty_col_indices: list[int] = []

        for row, line in enumerate(file):
            if '#' in line:
                galaxy_line = [c for c in line.strip()]

                for col, galaxy in enumerate(galaxy_line):
                    if galaxy == '#':
                        galaxies.append((row, col))

                image.append(galaxy_line)
            else:
                empty = [c for c in line.strip()]
                image.append(empty)
                empty_row_indices.append(row)

        for col in range(len(image[0])):
            if all(image[row][col] == '.' for row in range(len(image))):
                empty_col_indices.append(col)

        return image, galaxies, empty_row_indices, empty_col_indices


def get_expanded_galaxies(galaxies: list[tuple[int, int]], empty_row_indices: list[int], empty_col_indices: list[int], expansion_factor: int) -> list[tuple[int, int]]:
    expanded_galaxies = []

    for galaxy in galaxies:
        row, col = galaxy

        expanded_row = row
        expanded_col = col

        for row_index in empty_row_indices:
            if row > row_index:
                expanded_row += expansion_factor - 1

        for col_index in empty_col_indices:
            if col > col_index:
                expanded_col += expansion_factor - 1

        expanded_galaxies.append((expanded_row, expanded_col))

    return expanded_galaxies


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def get_shortest_distances(expanded_galaxies: list[tuple[int, int]]) -> list[int]:
    distances = []

    for g1, g2 in itertools.combinations(expanded_galaxies, r=2):
        r1, c1 = g1
        r2, c2 = g2

        distance = manhattan_distance(r1, c1, r2, c2)
        distances.append(distance)

    return distances


image, galaxies, empty_row_indices, empty_col_indices = parse_galaxies_image(
    filename)

expanded_galaxies = get_expanded_galaxies(
    galaxies, empty_row_indices, empty_col_indices, expansion_factor=2)  # expansion_factor=1000000 for part 2

distances = get_shortest_distances(expanded_galaxies)

print(sum(distances))

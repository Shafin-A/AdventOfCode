def parse_input(filename: str):
    coordinates: dict[str, list[tuple[int, int]]] = {}
    grid: list[str] = []

    with open(filename) as file:
        for row, line in enumerate(file):
            line = line.rstrip()
            grid.append(line)

            for col, c in enumerate(line):
                if c != '.':
                    if c not in coordinates:
                        coordinates[c] = []

                    coordinates[c].append((row, col))

    return grid, coordinates


def get_antinode(coordinate_1: tuple[int, int], coordinate_2: tuple[int, int], grid: list[str], antinodes: set[tuple[int, int]]):
    r1, c1 = coordinate_1
    r2, c2 = coordinate_2
    dr = r2 + (r2 - r1)
    dc = c2 + (c2 - c1)

    if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
        antinodes.add((dr, dc))


def get_antinode_updated(coordinate_1: tuple[int, int], coordinate_2: tuple[int, int], grid: list[str], antinodes: set[tuple[int, int]]):
    r1, c1 = coordinate_1
    r2, c2 = coordinate_2
    dr = r2 + (r2 - r1)
    dc = c2 + (c2 - c1)

    antinodes.add((r2, c2))

    while 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
        antinodes.add((dr, dc))
        dr += r2 - r1
        dc += c2 - c1


def get_antinodes(grid: list[str], coordinates: dict[str, list[tuple[int, int]]], is_updated: bool):
    antinodes: set[tuple[int, int]] = set()

    for antenna in coordinates:
        antenna_coordinates = coordinates[antenna]

        for i in range(len(antenna_coordinates)):
            for j in range(i):
                coord_1 = antenna_coordinates[i]
                coord_2 = antenna_coordinates[j]

                if is_updated:
                    get_antinode_updated(coord_1, coord_2, grid, antinodes)
                    get_antinode_updated(coord_2, coord_1, grid, antinodes)
                else:
                    get_antinode(coord_1, coord_2, grid, antinodes)
                    get_antinode(coord_2, coord_1, grid, antinodes)

    return antinodes


if __name__ == "__main__":
    filename = "input.txt"

    grid, coordinates = parse_input(filename)

    antinodes = get_antinodes(grid, coordinates, False)
    print(len(antinodes))

    antinodes_updated = get_antinodes(grid, coordinates, True)
    print(len(antinodes_updated))

def parse_input(filename: str) -> tuple[list[list[str]], tuple[int, int]]:
    grid = []
    starting_point = (-1, -1)
    with open(filename) as file:
        for i, line in enumerate(file):
            grid.append([])
            for c in line.rstrip():
                grid[i].append(c)

            if "^" in line:
                starting_point = (i, line.index("^"))

    return grid, starting_point


def get_visited(grid: list[list[str]], starting_point: tuple[int, int]):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    row, col = starting_point

    visited = set()
    is_in_grid = True

    while is_in_grid:
        current_direction = directions[direction_index]
        dr, dc = current_direction

        if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
            if grid[row + dr][col + dc] == "#":
                direction_index = (direction_index + 1) % 4
                current_direction = directions[direction_index]
                dr, dc = current_direction

        visited.add((row, col))
        row += dr
        col += dc

        is_in_grid = 0 <= row < len(grid) and 0 <= col < len(grid[0])

    return visited


def has_cycle(grid: list[list[str]], starting_point: tuple[int, int]) -> bool:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0

    row, col = starting_point
    visited = set()

    while True:
        current_state = (row, col, direction_index)
        if current_state in visited:
            return True

        visited.add(current_state)

        current_direction = directions[direction_index]
        dr, dc = current_direction

        if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
            if grid[row + dr][col + dc] == "#":
                direction_index = (direction_index + 1) % 4
            else:
                row += dr
                col += dc
        else:
            return False


def calculate_possible_cycles(grid: list[list[str]], starting_point: tuple[int, int], visited: tuple[int, int]) -> int:
    num_cycles = 0

    for (row, col) in visited:
        if grid[row][col] != "#" and grid[row][col] != "^":
            grid[row][col] = '#'

            if has_cycle(grid, starting_point):
                num_cycles += 1

            grid[row][col] = '.'

    return num_cycles


if __name__ == "__main__":
    filename = "input.txt"

    grid, starting_point = parse_input(filename)

    visited = get_visited(grid, starting_point)
    num_cycles = calculate_possible_cycles(grid, starting_point, visited)

    print(len(visited))
    print(num_cycles)

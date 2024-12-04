def parse_input(filename: str) -> list[str]:
    grid = []

    with open(filename) as file:
        for line in file:
            grid.append(line.rstrip())

    return grid


def count_xmas(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # horizontal
    for row in grid:
        count += row.count("XMAS")
        count += row.count("SAMX")

    # vertical
    for col in range(cols):
        col_str = "".join(grid[row][col] for row in range(rows))
        count += col_str.count("XMAS")
        count += col_str.count("SAMX")

    # top-left to bottom-right
    for start_row in range(rows):
        diagonal = []
        r, c = start_row, 0
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count("XMAS")
        count += diagonal_str.count("SAMX")

    for start_col in range(1, cols):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count("XMAS")
        count += diagonal_str.count("SAMX")

    # top-right to bottom-left
    for start_row in range(rows):
        diagonal = []
        r, c = start_row, cols - 1
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count("XMAS")
        count += diagonal_str.count("SAMX")

    for start_col in range(cols - 2, -1, -1):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count("XMAS")
        count += diagonal_str.count("SAMX")

    return count


def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                if grid[i - 1][j - 1] + grid[i + 1][j + 1] in ["MS", "SM"]:
                    if grid[i - 1][j + 1] + grid[i + 1][j - 1] in ["MS", "SM"]:
                        count += 1

    return count


if __name__ == "__main__":
    filename = "input.txt"

    grid = parse_input(filename)

    print(count_xmas(grid))
    print(count_x_mas(grid))

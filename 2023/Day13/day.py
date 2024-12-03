ROW_MULTIPLIER = 100
COLUMN_MULTIPLIER = 1

with open("input.txt", "r") as file:
    grids = file.read().strip().split("\n\n")


def find_reflected_rows(grid, smudges=0):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        # Checking if there is exactly a certain amount of smudges (a difference between
        # corresponding elements) between the rows `above` and `below`. It does this by iterating over
        # each pair of corresponding elements in `above` and `below` and counting the number of
        # differences. If the count is equal to smudges, it means there is exactly that amount of smudges
        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                # x, y are the rows
                for x, y in zip(above, below)
            )
            == smudges
        ):
            return r

    return 0


solution1 = 0
solution2 = 0
for grid in grids:
    block = grid.splitlines()
    solution1 += find_reflected_rows(block) * ROW_MULTIPLIER
    solution2 += find_reflected_rows(block, smudges=1) * ROW_MULTIPLIER

    # transpose
    block = list(zip(*block))

    solution1 += find_reflected_rows(block) * COLUMN_MULTIPLIER
    solution2 += find_reflected_rows(block, smudges=1) * COLUMN_MULTIPLIER

print("Solution 1:", solution1)
print("Solution 2:", solution2)

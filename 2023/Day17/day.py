import heapq

filename = "input.txt"


def parse_grid(filename: str):
    with open(filename) as file:
        grid: list[list[int]] = []
        for line in file:
            line = [int(c) for c in line.strip()]
            grid.append(line)

        return grid


def shortest_path_with_constraints(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    # (cost, row, col, consecutive_moves, prev_direction, path)
    pq: list[tuple[int, int, int, int, tuple[int, int]]] = [
        (0, 0, 0, 0, (0, 0))
    ]

    visited: set[tuple[int, int, int, tuple[int, int]]] = set()

    while pq:
        cost, row, col, consecutive_moves, prev_direction = heapq.heappop(
            pq)

        if row == rows - 1 and col == cols - 1:
            return cost

        # Check if the current cell with consecutive moves information has been visited
        if (row, col, consecutive_moves, prev_direction) in visited:
            continue

        # Mark the current cell as visited
        visited.add((row, col, consecutive_moves, prev_direction))

        # Explore all possible directions
        for dr, dc in directions:

            if prev_direction == (-dr, -dc):
                continue

            if (dr, dc) == prev_direction:
                new_consecutive_moves = consecutive_moves + 1
            else:
                new_consecutive_moves = 1

            new_row, new_col = row + dr, col + dc

            # Check if the new position is within the grid
            if 0 <= new_row < rows and 0 <= new_col < cols:

                # Check if consecutive_moves is greater than 3
                if new_consecutive_moves <= 3:
                    new_cost = cost + grid[new_row][new_col]

                    # Add the new position to the priority queue
                    heapq.heappush(pq, (new_cost, new_row, new_col,
                                        new_consecutive_moves, (dr, dc)))

    # If the destination is not reachable
    return -1


grid = parse_grid(filename)
min_cost = shortest_path_with_constraints(grid)


print(min_cost)

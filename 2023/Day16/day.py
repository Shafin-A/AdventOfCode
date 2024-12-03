from enum import Enum
from collections import deque


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


filename = "input.txt"


def parse_layout(filename: str):
    with open(filename) as file:
        layout = []
        for line in file:
            layout.append(line.strip())
        return layout


def q_right(layout, q, row, col, visited):
    if col+1 < len(layout) and (row, col+1, Direction.RIGHT) not in visited:
        q.append((row, col+1, layout[row][col+1], Direction.RIGHT))


def q_left(layout, q, row, col, visited):
    if col-1 >= 0 and (row, col-1, Direction.LEFT) not in visited:
        q.append((row, col-1, layout[row][col-1], Direction.LEFT))


def q_up(layout, q, row, col, visited):
    if row-1 >= 0 and (row-1, col, Direction.UP) not in visited:
        q.append((row-1, col, layout[row-1][col], Direction.UP))


def q_down(layout, q, row, col, visited):
    if row+1 < len(layout[0]) and (row+1, col, Direction.DOWN) not in visited:
        q.append((row+1, col, layout[row+1][col], Direction.DOWN))


def BFS_traverse(layout: list[str], start_point):
    q: deque[tuple[int, int, str, Enum]] = deque()

    visited = set()
    visited_without_direction = set()

    q.append(start_point)

    while (not len(q) == 0):
        node = q.popleft()
        row, col, char, direction = node

        visited.add((row, col, direction))
        visited_without_direction.add((row, col))

        if char == '.':
            if direction == Direction.RIGHT:
                q_right(layout, q, row, col, visited)
            elif direction == Direction.LEFT:
                q_left(layout, q, row, col, visited)
            elif direction == Direction.UP:
                q_up(layout, q, row, col, visited)
            elif direction == Direction.DOWN:
                q_down(layout, q, row, col, visited)

        elif char == '\\':
            if direction == Direction.RIGHT:
                q_down(layout, q, row, col, visited)
            elif direction == Direction.LEFT:
                q_up(layout, q, row, col, visited)
            elif direction == Direction.UP:
                q_left(layout, q, row, col, visited)
            elif direction == Direction.DOWN:
                q_right(layout, q, row, col, visited)

        elif char == '/':
            if direction == Direction.RIGHT:
                q_up(layout, q, row, col, visited)
            elif direction == Direction.LEFT:
                q_down(layout, q, row, col, visited)
            elif direction == Direction.UP:
                q_right(layout, q, row, col, visited)
            elif direction == Direction.DOWN:
                q_left(layout, q, row, col, visited)

        elif char == '|':
            if direction == Direction.RIGHT:
                q_up(layout, q, row, col, visited)
                q_down(layout, q, row, col, visited)
            elif direction == Direction.LEFT:
                q_up(layout, q, row, col, visited)
                q_down(layout, q, row, col, visited)
            elif direction == Direction.UP:
                q_up(layout, q, row, col, visited)
            elif direction == Direction.DOWN:
                q_down(layout, q, row, col, visited)

        elif char == '-':
            if direction == Direction.RIGHT:
                q_right(layout, q, row, col, visited)
            elif direction == Direction.LEFT:
                q_left(layout, q, row, col, visited)
            elif direction == Direction.UP:
                q_left(layout, q, row, col, visited)
                q_right(layout, q, row, col, visited)
            elif direction == Direction.DOWN:
                q_left(layout, q, row, col, visited)
                q_right(layout, q, row, col, visited)

    return visited_without_direction


def part_1(layout):
    start_point = (0, 0, layout[0][0], Direction.RIGHT)
    visited = BFS_traverse(layout, start_point)

    return len(visited)


def part_2(layout):
    rows = len(layout)
    cols = len(layout[0]) if rows > 0 else 0

    visiteds = []

    # Traverse corners
    top_left_right = BFS_traverse(
        layout, (0, 0, layout[0][0], Direction.RIGHT))
    top_left_down = BFS_traverse(layout, (0, 0, layout[0][0], Direction.DOWN))

    bottom_right_up = BFS_traverse(
        layout, (rows-1, 0, layout[rows-1][0], Direction.UP))
    bottom_right_left = BFS_traverse(
        layout, (rows-1, 0, layout[rows-1][0], Direction.LEFT))

    top_right_left = BFS_traverse(
        layout, (0, cols-1, layout[0][cols-1], Direction.LEFT))
    top_right_down = BFS_traverse(
        layout, (0, cols-1, layout[0][cols-1], Direction.DOWN))

    bottom_left_up = BFS_traverse(
        layout, (rows-1, cols-1, layout[rows-1][cols-1], Direction.UP))
    bottom_left_right = BFS_traverse(
        layout, (rows-1, cols-1, layout[rows-1][cols-1], Direction.RIGHT))

    visiteds.append(len(top_left_right))
    visiteds.append(len(top_left_down))

    visiteds.append(len(bottom_right_up))
    visiteds.append(len(bottom_right_left))

    visiteds.append(len(top_right_left))
    visiteds.append(len(top_right_down))

    visiteds.append(len(bottom_left_up))
    visiteds.append(len(bottom_left_right))

    # Traverse top row
    for i in range(1, cols - 1):
        visited = BFS_traverse(layout, (0, i, layout[0][i], Direction.DOWN))
        visiteds.append(len(visited))

    # Traverse right column (excluding the first and last elements to avoid duplicates)
    for i in range(1, rows - 1):
        visited = BFS_traverse(
            layout, (i, cols-1, layout[i][cols-1], Direction.LEFT))
        visiteds.append(len(visited))

    # Traverse bottom row (in reverse order to avoid duplicates) and mark bottom-right corner
    for i in range(cols - 1, -1, -1):
        visited = BFS_traverse(
            layout, (rows-1, i, layout[rows-1][i], Direction.UP))
        visiteds.append(len(visited))

    # Traverse left column (excluding the first and last elements to avoid duplicates) and mark top-right and bottom-left corners
    for i in range(rows - 2, 0, -1):
        visited = BFS_traverse(
            layout, (i, 0, layout[i][0], Direction.RIGHT))
        visiteds.append(len(visited))

    return max(visiteds)


# for i, li in enumerate(layout):
#     for j, lj in enumerate(li):
#         if (i, j) in visited:
#             print('#', end="")
#         else:
#             print('.', end="")
#     print()
# print()
layout = parse_layout(filename)

print(part_1(layout))
print(part_2(layout))

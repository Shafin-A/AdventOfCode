from queue import SimpleQueue

filename = "input.txt"


def parse_pipes(filename) -> tuple[list[list[str]], tuple[int, int]]:
    with open(filename) as file:
        pipes = []
        start_point = (-1, -1)

        for row, line in enumerate(file):
            line.translate(str.maketrans("-|F7LJ.", "─│┌┐└┘ "))
            nodes = [c for c in line.strip()]
            pipes.append(nodes)

            if 'S' in line:
                col = line.find('S')
                start_point = (row, col)

        return pipes, start_point


def get_edges(pipes: list[list[str]], node_coords: tuple[int, int, int], visited: set[tuple[int, int]]):

    row, col, depth = node_coords

    node = pipes[row][col]
    edges: list[tuple[int, int, int]] = []

    # print(node)

    match node:
        case '|':
            up_node = (row-1, col, depth + 1)
            if (row-1, col) not in visited:
                up_symbol = pipes[row-1][col]
                if up_symbol in '7|F':
                    edges.append(up_node)
                    visited.add((row-1, col))

            down_node = ((row+1, col, depth + 1))
            if (row+1, col) not in visited:
                down = pipes[row+1][col]
                if down in 'J|L':
                    edges.append(down_node)
                    visited.add((row+1, col))

        case '-':
            left_node = (row, col-1, depth + 1)
            if (row, col-1) not in visited:
                left = pipes[row][col-1]
                if left in 'L-F':
                    edges.append(left_node)
                    visited.add((row, col-1))

            right_node = (row, col+1, depth + 1)
            if (row, col+1) not in visited:
                right = pipes[row][col+1]
                if right in 'J-7':
                    edges.append(right_node)
                    visited.add((row, col+1))

        case 'L':
            up_node = (row-1, col, depth + 1)
            if (row-1, col) not in visited:
                up_symbol = pipes[row-1][col]
                if up_symbol in '7|F':
                    edges.append(up_node)
                    visited.add((row-1, col))

            right_node = (row, col+1, depth + 1)
            if (row, col+1) not in visited:
                right = pipes[row][col+1]
                if right in 'J-7':
                    edges.append(right_node)
                    visited.add((row, col+1))

        case 'J':
            up_node = (row-1, col, depth + 1)
            if (row-1, col) not in visited:
                up_symbol = pipes[row-1][col]
                if up_symbol in '7|F':
                    edges.append(up_node)
                    visited.add((row-1, col))

            left_node = (row, col-1, depth + 1)
            if (row, col-1) not in visited:
                left = pipes[row][col-1]
                if left in 'L-F':
                    edges.append(left_node)
                    visited.add((row, col-1))

        case '7':
            down_node = (row+1, col, depth + 1)
            if (row+1, col) not in visited:
                down = pipes[row+1][col]
                if down in 'J|L':
                    edges.append(down_node)
                    visited.add((row+1, col))

            left_node = (row, col-1, depth + 1)
            if (row, col-1) not in visited:
                left = pipes[row][col-1]
                if left in 'L-F':
                    edges.append(left_node)
                    visited.add((row, col-1))

        case 'F':
            down_node = (row+1, col, depth + 1)
            if (row+1, col) not in visited:
                down = pipes[row+1][col]
                if down in 'J|L':
                    edges.append(down_node)
                    visited.add((row+1, col))

            right_node = (row, col+1, depth + 1)
            if (row, col+1) not in visited:
                right = pipes[row][col+1]
                if right in 'J-7':
                    edges.append(right_node)
                    visited.add((row, col+1))

    return edges


def max_depth_BFS(pipes: list[list[str]], start_point: tuple[int, int]) -> int:
    q: SimpleQueue[tuple[int, int, int]] = SimpleQueue()
    start_row, start_col = start_point

    q.put((start_row, start_col, 0))

    visited = set()

    max_depth = 0
    while (not q.empty()):
        node = q.get()
        row, col, _ = node
        visited.add((row, col))

        edges = get_edges(pipes, node, visited)

        for edge in edges:
            (_, _, depth) = edge

            if depth > max_depth:
                max_depth = depth
            q.put(edge)

    return max_depth


pipes, start_point = parse_pipes(filename)

max_depth = max_depth_BFS(pipes, (107, 110))
print(max_depth)
# print(start_point)


with open(filename) as file:
    pipes = "".join(file.readlines())

    pipes = pipes.translate(str.maketrans("-|F7LJ.", "─│┌┐└┘·"))

    print(pipes)

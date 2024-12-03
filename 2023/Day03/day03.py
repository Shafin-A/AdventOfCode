filename = 'day03_input.txt'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __repr__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(repr(self))


def map_points(input_string: str, i: int, number_coordinates, symbol_coordinates) -> None:
    current_number = 0

    for col, char in enumerate(input_string):
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif current_number != 0:
            for j in range(col - len(str(current_number)), col):
                number_coordinates[Point(j, i)] = current_number
            current_number = 0

        if char != '.' and not char.isdigit():
            symbol_coordinates[Point(col, i)] = char

    # Check if the last part of the string forms a number
    if current_number != 0:
        for j in range(len(input_string) - len(str(current_number)), len(input_string)):
            number_coordinates[Point(j, i)] = current_number


def find_adjacent_points(point: Point, number_coordinates: dict[Point, int]) -> list[Point]:
    x, y = point.x, point.y
    target_number = number_coordinates[point]

    adjacent_points = []

    # Define possible neighboring coordinates
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for neighbor_x, neighbor_y in neighbors:
        neighbor_point = Point(neighbor_x, neighbor_y)

        # Check if the neighbor point is in the dictionary and has the same number
        if neighbor_point in number_coordinates and number_coordinates[neighbor_point] == target_number:
            adjacent_points.append(neighbor_point)

    return adjacent_points


number_coordinates: dict[Point, int] = {}
symbol_coordinates: dict[Point, str] = {}


with open(filename) as file:
    for i, line in enumerate(file):
        line = line.rstrip()

        map_points(line, i, number_coordinates, symbol_coordinates)


part_nums = []
seen_coords = set()

for coord in symbol_coordinates:
    if (symbol_coordinates[coord] == '*'):
        x, y = coord.x, coord.y

        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
                     (x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]

        to_add = []

        for neighbor_x, neighbor_y in neighbors:
            neighbor_point = Point(neighbor_x, neighbor_y)

            if neighbor_point not in seen_coords and neighbor_point in number_coordinates:
                # part_nums.append(number_coordinates[neighbor_point])
                to_add.append(number_coordinates[neighbor_point])

                seen_coords.add(neighbor_point)

                adjacent_points = find_adjacent_points(
                    neighbor_point, number_coordinates)

                for adjacent_point in adjacent_points:
                    seen_coords.add(adjacent_point)

        if (len(to_add) == 2):
            part_nums.append(to_add[0] * to_add[1])

print(sum(part_nums))

filename = 'day02_input.txt'


MAX_CUBES = {
    'RED': 12,
    'GREEN': 13,
    'BLUE': 14
}


class GameSet:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def __str__(self):
        return f"Red: {self.red}, Blue: {self.blue}, Green: {self.green}"


def create_game_sets(input_list) -> list[GameSet]:
    game_sets = []

    for item in input_list:
        red = 0
        blue = 0
        green = 0

        for pair in item:
            quantity, color = pair.split()
            quantity = int(quantity)

            if color == 'red':
                red += quantity
            elif color == 'blue':
                blue += quantity
            elif color == 'green':
                green += quantity

        game_set = GameSet(red, blue, green)
        game_sets.append(game_set)

    return game_sets


def get_game_id(line: str) -> int:

    [game_and_id, game] = line.split(':')

    game_id = game_and_id.split(' ')[1]

    game_results = [x.strip() for x in game.split(';')]
    game_results = [item.split(', ') for item in game_results]

    game_sets = create_game_sets(game_results)

    for game_set in game_sets:
        if game_set.red > MAX_CUBES['RED']:
            return 0
        if game_set.green > MAX_CUBES['GREEN']:
            return 0
        if game_set.blue > MAX_CUBES['BLUE']:
            return 0

    return int(game_id)


def get_min_power(line: str) -> int:

    game = line.split(':')[1]

    game_results = [x.strip() for x in game.split(';')]
    game_results = [item.split(', ') for item in game_results]

    game_sets = create_game_sets(game_results)

    max_red = -1
    max_green = -1
    max_blue = -1

    for game_set in game_sets:
        if game_set.red > max_red:
            max_red = game_set.red
        if game_set.green > max_green:
            max_green = game_set.green
        if game_set.blue > max_blue:
            max_blue = game_set.blue

    return max_red * max_blue * max_green


def sum_game_ids(filename: str) -> int:
    sum = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            sum += get_game_id(line)

    return sum


def sum_min_powers(filename: str) -> int:
    sum = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()

            sum += get_min_power(line)

    return sum


print(sum_game_ids(filename=filename))
print(sum_min_powers(filename=filename))

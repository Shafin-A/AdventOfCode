import re
filename = "input.txt"


def parse_input(filename):
    with open(filename) as file:
        boundaries = []

        start = (0, 0)

        directions = {
            '0': 'R',
            '1': 'D',
            '2': 'L',
            '3':  'U'
        }
        for line in file:
            line = line.strip().split()
            hex = line[2]

            hex = re.findall(r'#([a-fA-F0-9]+)', hex)[0]

            direction = directions[hex[-1]]

            hex = hex[:-1]

            num = int(hex, 16)

            if direction == 'R':
                for _ in range(num):
                    x, y = start
                    x += 1
                    start = (x, y)
                    boundaries.append((x, y))
            elif direction == 'D':
                for _ in range(num):
                    x, y = start
                    y += 1
                    start = (x, y)
                    boundaries.append((x, y))
            elif direction == 'L':
                for _ in range(num):
                    x, y = start
                    x -= 1
                    start = (x, y)
                    boundaries.append((x, y))
            elif direction == 'U':
                for _ in range(num):
                    x, y = start
                    y -= 1
                    start = (x, y)
                    boundaries.append((x, y))

        return boundaries


def shoelace_formula(polygonBoundary):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) *
         (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    return abs(sum(l) / 2.)


def picks_theorem(A, b):
    return (A+1) - (b/2)


boundaries = parse_input(filename)

A = shoelace_formula(boundaries)

print(A)

picks = picks_theorem(A, len(boundaries))

print(picks + len(boundaries))

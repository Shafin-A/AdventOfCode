
def p1():
    mappings = {
        'A X\n': 1 + 3,
        'A Y\n': 2 + 6,
        'A Z\n': 3 + 0,

        'B X\n': 1 + 0,
        'B Y\n': 2 + 3,
        'B Z\n': 3 + 6,

        'C X\n': 1 + 6,
        'C Y\n': 2 + 0,
        'C Z\n': 3 + 3,
    }

    file = open("Day2Input.txt", "r")

    score = 0
    for line in file:
        score += mappings[line]

    file.close()

    return score

print(p1())

def p2():
    mappings = {
        'A X\n': 0 + 3,
        'A Y\n': 3 + 1,
        'A Z\n': 6 + 2,

        'B X\n': 0 + 1,
        'B Y\n': 3 + 2,
        'B Z\n': 6 + 3,

        'C X\n': 0 + 2,
        'C Y\n': 3 + 3,
        'C Z\n': 6 + 1,
    }

    file = open("Day2Input.txt", "r")

    score = 0
    for line in file:
        score += mappings[line]

    file.close()

    return score

print(p2())
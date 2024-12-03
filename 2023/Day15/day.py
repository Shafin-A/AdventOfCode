import re

filename = "input.txt"


class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key} {self.value})"

    def __repr__(self):
        return f"({self.key} {self.value})"


def parse_input(filename: str):
    with open(filename) as file:
        line = file.readline().strip()

        words = line.split(',')

        return words


def HASH(string: str):
    current_value = 0

    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def HASHMAP(contents):
    boxes: list[list[Node] | None] = [None] * 256

    for content in contents:
        label = re.sub(r'[^a-z]', '', content)

        box_index = HASH(label)
        box = boxes[box_index]

        if '-' in content:
            if box is not None:
                for i, node in enumerate(box):
                    if node.key == label:
                        box.pop(i)
                        break

                if not box:
                    boxes[box_index] = None

        elif '=' in content:
            [key, value] = content.split('=')
            value = int(value)
            if box is not None:
                need_append = True

                for i, node in enumerate(box):
                    if node.key == key:
                        box[i].value = value
                        need_append = False
                        break
                if need_append:
                    box.append(Node(key, value))
            else:
                box = [Node(key, value)]
                boxes[box_index] = box

    return boxes


def part_1():
    contents = parse_input(filename)
    hashes = [HASH(content) for content in contents]

    return sum(hashes)


def part_2():
    contents = parse_input(filename)

    boxes = HASHMAP(contents)

    powers = [((i+1) * (j+1) * node.value) for i, box in enumerate(boxes)
              if box is not None for j, node in enumerate(box)]

    return sum(powers)


print(part_1())
print(part_2())

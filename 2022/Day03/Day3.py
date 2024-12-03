from string import ascii_letters

def p1():
    letter_mappings = {v:k+1 for k,v in enumerate(ascii_letters)}
    file = open("Day3Input.txt", "r") 

    priorities = 0
    for line in file:
        items = line.strip()

        first_part, second_part = items[:len(items)//2], items[len(items)//2:]

        first_part_unique = set(first_part)
        second_part_unique = set(second_part)

        both_parts_contain, = first_part_unique.intersection(second_part_unique)

        priorities += letter_mappings[both_parts_contain]

    file.close()

    return priorities

print(p1())

def p2():
    letter_mappings = {v:k+1 for k,v in enumerate(ascii_letters)}
    file = open("Day3Input.txt", "r") 

    priorities = 0
    items = [set(),set(),set()]
    for i, line in enumerate(file):
        item = line.strip()
        items[(i+1)%3] = set(item)

        if (i+1)%3 == 0:
            all_parts_contain = items[0]
            for item in items:
                all_parts_contain = all_parts_contain.intersection(item)

            all_parts_contains, = all_parts_contain

            priorities += letter_mappings[all_parts_contains]

    file.close()

    return priorities

print(p2())
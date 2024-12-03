import re

def p1():
    file = open("Day4Input.txt", "r") 

    count = 0

    for line in file:
        pair = line.strip()

        first_range_start, first_range_end, second_range_start, second_range_end = [int(i) for i in re.split('-|,', pair)]
        
        def range_contains(a: int, b: int, c: int, d: int):
            return (c <= a and d >= b) or (a <= c and b >= d)

        if (range_contains(first_range_start, first_range_end, second_range_start, second_range_end)):
            count += 1

    file.close()

    return count

print(p1())

def p2():
    file = open("Day4Input.txt", "r") 

    count = 0

    for line in file:
        pair = line.strip()

        first_range_start, first_range_end, second_range_start, second_range_end = [int(i) for i in re.split('-|,', pair)]
        
        def range_contains(a: int, b: int, c: int, d: int):
            return (d >= a >= c) or (b >= c >= a)


        if (range_contains(first_range_start, first_range_end, second_range_start, second_range_end)):
            count += 1

    file.close()

    return count

print(p2())
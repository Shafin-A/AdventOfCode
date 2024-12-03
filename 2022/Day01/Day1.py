
def p1():
    file = open("Day1Input.txt", "r")

    current_max = 0
    current_sum = 0

    for line in file:
        if line == "\n":
            current_max = max(current_max, current_sum)
            current_sum = 0

        else:
            current_sum += int(line)

    file.close()

    return current_max


def p2():
    file = open("Day1Input.txt", "r")

    current_max1 = 0
    current_max2 = 0
    current_max3 = 0
    current_sum = 0

    for line in file:
        if line == "\n":
            
            if current_sum > current_max1:
                current_max3 = current_max2
                current_max2 = current_max1
                current_max1 = current_sum

            elif current_sum > current_max2:
                current_max3 = current_max2
                current_max2 = current_sum
            
            elif current_sum > current_max3:
                current_max3 = current_sum
            
            current_sum = 0

        else:
            current_sum += int(line)

    file.close()

    return current_max1, current_max2, current_max3, (current_max1 + current_max2 + current_max3)

print(p1())
print(p2())
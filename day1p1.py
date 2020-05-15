import math

def fuel(mass):
    return math.floor(mass / 3) - 2

f = open("inputp1.txt", "r")

lines = f.readlines()

sum = 0
for line in lines:
    sum += fuel(int(line))

print(sum)

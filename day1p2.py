import math

def fuel_until_zero(mass, sum):
    fuel = math.floor(mass / 3) - 2

    if fuel <= 0:
        return sum
    else:
        sum += fuel
        return fuel_until_zero(fuel, sum)

f = open("inputp2.txt", "r")

lines = f.readlines()

sum = 0
for line in lines:
    sum += fuel_until_zero(int(line), 0)

print(sum)

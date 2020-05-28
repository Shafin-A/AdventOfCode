import math

f = open("input.txt", "r")
lines = f.readlines()

coords = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            coords.append((x, y))

def asteroids_slope(x, y, coords):
    def slope(x1, y1, x2, y2):
        # return slopes as ratios
        # slope y = mx + b
        # m = (y1 - y2) / (x1- x2) -> store as ratios
        # e.g. m = 6 / 2 -> (2, 6) -> (1, 3)
        # normalize by gcd since they're all ints
        gcd = math.gcd(x1 - x2, y1 - y2)
        ratio_x = (x1 - x2) / gcd
        ratio_y = (y1 - y2) / gcd

        return (ratio_x, ratio_y)
    
    slopes = set()
    for x1, y1 in coords:
        if (x1, y1) == (x, y):
            continue
        slopes.add(slope(x1, y1, x, y))
        
    return slopes

def asteroids_angle(x, y, coords):
    def angle(x1, y1, x2, y2):
          return (math.degrees(math.atan2(y1- y2, x1- x2)) + 90) % 360
        
    angles = dict()
    for x1, y1 in coords:
        angles.setdefault(angle(x1, y1, x, y), [])
        angles[angle(x1, y1, x, y)].append((x1, y1))

    return angles

# 2 different ways to get best asteroid
# by angle, or by slope
def best_asteroid(angle):
    max_asteroids = 0
    best_x = -1
    best_y = -1
    angles = None
    for x, y in coords:
        if angle:
            asteroids = len(asteroids_angle(x, y, coords))
        else:
            asteroids = len(asteroids_slope(x, y, coords))
        if asteroids > max_asteroids:
            max_asteroids = asteroids
            best_x = x
            best_y = y
    return max_asteroids, best_x, best_y

max_asteroids, best_x, best_y = best_asteroid(True) # True - by angles, False - by slope
print("Max asteroids = " + str(max_asteroids) + " at (" + str(best_x) + ", " + str(best_y) + ")")

def vaporize(best_x, best_y, coords):
    angles = asteroids_angle(best_x, best_y, coords)
    sorted_coords = sorted(angles.items())
    
    cnt = 0
    for (_, coord) in sorted_coords:
        if coord == []:
            continue
        c = coord.pop(0)
        cnt += 1
        if cnt == 200:
            return c

    return None

vaporized = vaporize(best_x, best_y, coords)
if vaporized == None:
    print("Vaporized all asteroids before 200th!")
else:
    print("200th vaporized asteroid at " + str(vaporized))













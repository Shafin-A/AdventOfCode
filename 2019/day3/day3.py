def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def build_path(path):
    coords = []
    x = 0
    y = 0
    
    for dir in path:
        if dir[0] == 'R':
            right = int(dir[1:])
            for i in range(right):
                coords.append((x + i, y))
            x += right
        if dir[0] == 'L':
            left = int(dir[1:])
            for i in range(left):
                coords.append((x - i, y))
            x -= left
        if dir[0] == 'U':
            up = int(dir[1:])
            for i in range(up):
                coords.append((x, y + i))
            y += up
        if dir[0] == 'D':
            down = int(dir[1:])
            for i in range(down):
                coords.append((x, y - i))
            y -= down
    return coords
        
f = open("input.txt", "r")

path_1 = f.readline().split(",")
path_2 = f.readline().split(",")

coords_1 = build_path(path_1)
coords_2 = build_path(path_2)

## this is very slowwww, but it works!
##min_dist = 9999999
##for i in coords_1:
##    for j in coords_2:
##        print(i, j)
##        if i == j:
##            if i == (0, 0) or j == (0, 0):
##                continue
##            x, y = i
##
##            dist = manhattan(x, y, 0, 0)
##            if dist < min_dist:
##                min_dist = dist

intersect = set(coords_1).intersection(coords_2)
intersect = intersect.difference([(0,0)])

min_dist = 99999
for x,y in intersect:
    dist = manhattan(x, y, 0, 0)
    if dist < min_dist:
        min_dist = dist

combined_steps = []
for i in intersect:
    combined_steps.append(coords_1.index(i) + coords_2.index(i))

print(min_dist)
print(min(combined_steps))


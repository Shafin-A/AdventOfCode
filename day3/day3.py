def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def build_path(path):
    coords = []
    x = 0
    y = 0
    for dir in path:
        if dir[0] == 'R':
            right = int(dir[1 : len(dir)])
            for i in range(right):
                coords.append((x + i, y))
            x += right
        if dir[0] == 'L':
            left = int(dir[1 : len(dir)])
            for i in range(left):
                coords.append((x - i, y))
            x -= left
        if dir[0] == 'U':
            up = int(dir[1 : len(dir)])
            for i in range(up):
                coords.append((x, y + i))
            y += up
        if dir[0] == 'D':
            down = int(dir[1 : len(dir)])
            for i in range(down):
                coords.append((x, y - i))
            y -= down
        coords.append((x, y))
    return coords
        


f = open("input.txt", "r")

path_1 = f.readline().split(",")
path_2 = f.readline().split(",")

coords_1 = build_path(path_1)
coords_2 = build_path(path_2)

min_dist = 9999999
for i in coords_1:
    for j in coords_2:
        if i == (0, 0) or j == (0, 0):
            continue
        if i == j:
            x, y = i

            dist = manhattan(x, y, 0, 0)
            if dist < min_dist:
                min_dist = dist

print(min_dist)

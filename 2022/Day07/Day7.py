from collections import defaultdict

def cd(dir, stack):
    if stack == '/':
        stack = ['/']
    elif dir == '..':
        stack.pop()
    else:
       stack.append(dir)
    
    return stack


directory_stack = []
sizes = defaultdict(int)

lines = open("Day7Input.txt", "r")

for line in lines:
    splitted = line.split()
    if splitted[0] == '$' and splitted[1] == 'cd':
        directory_stack = cd(splitted[2], directory_stack)
    if splitted[0].isdigit():
        file_size = int(splitted[0])

        for i in range(len(directory_stack)):
            dir = '/'.join(directory_stack[:i+1]).replace("//", "/")
            sizes[dir] += file_size


sum = 0
for _, size in sizes.items():
    if size < 100000:
        sum += size

print(sum)

total_disk_space = 70000000
needed_disk_space = 30000000
space_to_free = sizes['/'] + needed_disk_space - total_disk_space

min_size = 70000000
for _, size in sizes.items():
    if size >= space_to_free:
        if size < min_size:
            min_size = size

print(min_size)
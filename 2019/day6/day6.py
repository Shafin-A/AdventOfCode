f = open("input.txt","r")
lines = f.readlines()

orbits = {}
planets = set()
graph = {}

for line in lines:
    split = line.rstrip().split(")")
    
    planets.add(split[0])
    planets.add(split[1])
    
    orbits.setdefault(split[0], set())
    orbits[split[0]].add(split[1])

    graph.setdefault(split[0], set())
    graph.setdefault(split[1], set())
    graph[split[0]].add(split[1])
    graph[split[1]].add(split[0])



######## PART 1 ########
def count_orbits(planet, count):
    for k, v in orbits.items():
        if planet in v:
            return count_orbits(k, count+1)

    return count

count = 0
for planet in planets:
    count += count_orbits(planet, 0)
    
print(count)

######## PART 2 ########

# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
 
    if start == goal:
        return 0
 
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return len(new_path)
 
            visited.append(node) 


you_parent = ""
san_parent = ""

for k, v in orbits.items():
    if "YOU" in v:
        you_parent = k
    if "SAN" in v:
        san_parent = k

print(bfs(graph, you_parent, san_parent) - 1)

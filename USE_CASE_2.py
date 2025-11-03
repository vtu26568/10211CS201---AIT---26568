# Map Navigation using Heuristic Search (Greedy Best-First Search)

# Graph Representation
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'D': 5, 'E': 12},
    'C': {'F': 7},
    'D': {},
    'E': {'G': 3},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values (estimated cost to reach goal 'G')
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 2,
    'G': 0
}

# Heuristic Search Function
def heuristic_search(graph, heuristics, start, goal):
    open_list = [start]
    closed_list = []
    path = []

    while open_list:
        current = min(open_list, key=lambda node: heuristics[node])
        open_list.remove(current)
        closed_list.append(current)
        path.append(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)

    return None

# Initial and Goal States
start = 'A'
goal = 'G'

# Execute the search
path = heuristic_search(graph, heuristics, start, goal)

# Print the Result
print("Path found using Heuristic Search:")
for city in path:
    print(city)

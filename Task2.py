import random
def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]
    return cost
def hill_climbing_tsp(graph):
    V = len(graph)
    current_path = list(range(V))
    random.shuffle(current_path)
    current_cost = calculate_cost(current_path, graph)
    improved = True
    while improved:
        improved = False
        for i in range(V):
            for j in range(i + 1, V):
                neighbor = current_path[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor_cost = calculate_cost(neighbor, graph)
                if neighbor_cost < current_cost:
                    current_path, current_cost = neighbor, neighbor_cost
                    improved = True
    return current_path, current_cost
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
if __name__ == "__main__":
    print("Task 2: Implementation of Hill Climbing Algorithm for Heuristic Search Approach\n")
    best_path, best_cost = hill_climbing_tsp(graph)
    print("Best Path Found:", best_path)
    print("Minimum Cost:", best_cost)

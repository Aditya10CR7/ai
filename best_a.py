# best A*
import heapq

# Define the graph as a dictionary of nodes and their neighbors
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

# Define the heuristic function as the straight-line distance to the goal node
heuristic = {
    'A': 8,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 0
}

# Define the function to implement Best-First Search algorithm
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    queue = [(heuristic[start], start)]
    while queue:
        (f, current_node) = heapq.heappop(queue)
        if current_node == goal:
            return f
        visited.add(current_node)
        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
    return None

# Define the function to implement A* algorithm
def astar_search(graph, start, goal, heuristic):
    visited = set()
    g_scores = {start: 0}
    f_scores = {start: heuristic[start]}
    queue = [(f_scores[start], start)]
    while queue:
        (f, current_node) = heapq.heappop(queue)
        if current_node == goal:
            return f
        visited.add(current_node)
        for neighbor, distance in graph[current_node].items():
            if neighbor in visited:
                continue
            tentative_g_score = g_scores[current_node] + distance
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic[neighbor]
                heapq.heappush(queue, (f_scores[neighbor], neighbor))
    return None

# Prompt the user to enter the start and goal nodes
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

# Find the path using Best-First Search
best_first_path_cost = best_first_search(graph, start, goal, heuristic)
if best_first_path_cost is not None:
    print(f"The path found by Best-First Search has a cost of {best_first_path_cost}")
else:
    print(f"There is no path from {start} to {goal} using Best-First Search")

# Find the path using A*
astar_path_cost = astar_search(graph, start, goal, heuristic)
if astar_path_cost is not None:
    print(f"The path found by A* has a cost of {astar_path_cost}")
else:
    print(f"There is no path from {start} to {goal} using A*")


import heapq

def best_first_search(graph, start, goal, heuristic):
    heap = [(heuristic(start, goal), start)]
    visited = set()

    while heap:
        (f, node) = heapq.heappop(heap)

        if node == goal:
            return visited

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (heuristic(neighbor, goal), neighbor))

    return visited

# Get user input for graph
graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbors = input("Enter the neighbors of " + node + " separated by commas: ").split(",")
    graph[node] = set(neighbors)

# Get user input for starting and ending nodes
start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

# Define a heuristic function (in this case, the shortest distance between two nodes)
def heuristic(node, goal):
    distances = {'A': 8, 'B': 5, 'C': 3, 'D': 2, 'E': 4, 'F': 1}
    return distances[node]

# Perform Best-First Search and print result
print(best_first_search(graph, start_node, goal_node, heuristic))

import heapq

def a_star_search(graph, start, goal, heuristic):
    heap = [(0, start)]
    visited = set()
    g_scores = {start: 0}

    while heap:
        (f, node) = heapq.heappop(heap)

        if node == goal:
            return visited

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node].items():
                g_score = g_scores[node] + cost
                if neighbor not in g_scores or g_score < g_scores[neighbor]:
                    g_scores[neighbor] = g_score
                    f_score = g_score + heuristic(neighbor, goal)
                    heapq.heappush(heap, (f_score, neighbor))

    return visited

# Get user input for graph
graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbors = input("Enter the neighbors of " + node + " separated by commas: ").split(",")
    edges = {}
    for neighbor in neighbors:
        cost = int(input("Enter the cost of the edge between " + node + " and " + neighbor + ": "))
        edges[neighbor] = cost
    graph[node] = edges

# Get user input for starting and ending nodes
start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

# Define a heuristic function (in this case, the shortest distance between two nodes)
def heuristic(node, goal):
    distances = {'A': 8, 'B': 5, 'C': 3, 'D': 2, 'E': 4, 'F': 1}
    return distances[node]

# Perform A* Search and print result
print(a_star_search(graph, start_node, goal_node, heuristic))

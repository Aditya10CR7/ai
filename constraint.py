# # constraint

def graph_coloring(graph):
    colors = {}  # dictionary to store the assigned colors for each node
    for node in graph:
        used_colors = {colors.get(neighbour) for neighbour in graph[node]}
        available_colors = set(range(len(graph))) - used_colors
        color = min(available_colors)
        colors[node] = color
    return colors

# Example usage:
graph = {}
n = int(input("Enter the number of nodes in the graph: "))
for i in range(n):
    adj_list = list(map(int, input(f"Enter the adjacent nodes of node {i}: ").split()))
    graph[i] = adj_list
colors = graph_coloring(graph)
print(colors)

# --------------------------------------------------------------------------
# # A function to print the color configuration.
# def printConfiguration(colorArray):
#     print("The assigned colors are as follows:")
#     for i in range(4):
#         print("Vertex: ",
#               i, " Color: ", colorArray[i])


# """
# A function that will check if the current colorArray of the graph is safe or not.
# """


# def isSafe(graph, colorArray):
#     for i in range(4):
#         for j in range(i + 1, 4):
#             if (graph[i][j] and colorArray[j] == colorArray[i]):
#                 return False
#     return True


# """
# A recursive function that takes the current index, number of vertices, and the color array. If the recursive call returns true then the coloring is possible. It returns
# false if the m colors cannot be assigned.
# """


# def graphColoringAlgorithm(graph, m, i, colorArray):
#     # If we have reached the last vertex then check and print the configuration.
#     if (i == 4):
#         if (isSafe(graph, colorArray)):
#             printConfiguration(colorArray)
#             return True
#         return False

#     # Assigning color to the vertex and recursively calling the function.
#     for j in range(1, m + 1):
#         colorArray[i] = j
#         if (graphColoringAlgorithm(graph, m, i + 1, colorArray)):
#             return True
#         colorArray[i] = 0
#     return False


# if __name__ == '__main__':
#     graph = [
#         [0, 1, 1, 1],
#         [1, 0, 1, 0],
#         [1, 1, 0, 1],
#         [1, 0, 1, 0],
#     ]
#     m = 3

#     # Initially the color list is initialized with 0.
#     colorArray = [0 for i in range(4)]

#     if (graphColoringAlgorithm(graph, m, 0, colorArray)):
#         print("Coloring is possible!")
#     else:
#         print("Coloring is not possible!")


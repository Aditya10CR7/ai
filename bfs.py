# bfs find nearest 2 from 1
from collections import deque
def nearest_position_of_2(matrix, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
    queue = deque([(row, col)])
    visited = set((row, col))
    while queue:
        x, y = queue.popleft()
        if matrix[x][y] == 2:
            return (x, y)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    return None
matrix = [[0, 2, 0], [1, 0, 0], [0, 0, 2]]
start_col = 0
start_row = 1
nearest_2 = nearest_position_of_2(matrix, start_row, start_col)
print(nearest_2) # (0, 2)
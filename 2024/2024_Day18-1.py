import copy
import random
import math
import itertools
import collections
import time
start_time = time.time()
# import sys
# sys.setrecursionlimit(3500)

input = open("inputs/2024_18.txt", "r+").read().splitlines()

total = 10**8

GRID_SIZE = 71
BYTES_READ = 1024

grid = [[" " for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

px, py = 0, 0
gx, gy = 0, 0
visited = []

for i in range(min(BYTES_READ, len(input))):
    c, r = input[i].split(",")
    c = int(c)
    r = int(r)

    grid[r][c] = "#"

    # print(input[i])

def print_grid(grid, visited):
    g = copy.deepcopy(grid)

    for x, y in visited:
        g[x][y] = "•"
    for l in g:
        print("".join(l))

visited = {}
def bfs(curr, distance):

    global visited
    global total
    print(distance, curr)

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    next_layer = []

    while curr:
        px, py = curr.pop()
        for dir in directions:
            dx, dy = dir

            # New, player, displacement
            nx = px + dx
            ny = py + dy

            # Stop if going out of bounds
            if nx < 0 or nx >= GRID_SIZE or ny < 0 or ny >= GRID_SIZE:
                continue

            # Stop if this is blocked
            if grid[nx][ny] == "#":
                continue

            # If we've already been here
            if (nx, ny) in visited.keys():
                if visited[(nx, ny)] > distance:
                    visited[(nx, ny)] = distance
                else:
                    continue

            if (nx, ny) not in next_layer:
                next_layer.append((nx, ny))
            visited[(nx, ny)] = distance+1

    if next_layer:
        bfs(next_layer, distance+1)

bfs([(0, 0)], 0)




g = copy.deepcopy(grid)
for key, value in visited.items():
    x, y = key
    g[x][y] = str(value % 10)
for l in g:
    print("".join(l))

for l in grid:
    print("".join(l))

print(visited)
print(visited[(GRID_SIZE-1, GRID_SIZE-1)])



# for l in grid:
#     print("".join(l))

print(f"Time elapsed: {time.time() - start_time}s")
import copy
import random
import math
import itertools
import collections
import time
start_time = time.time()
import sys
sys.setrecursionlimit(3500)

input = open("inputs/2024_18.txt", "r+").read().splitlines()


GRID_SIZE = 71
BYTES_READ = 1024

grid = [[" " for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

px, py = 0, 0
gx, gy = 0, 0

def bfs(curr, distance):

    global visited
    # print(distance, curr)

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


# Drop the first 1024 bits
for i in range(0, 1025):
    c, r = input[i].split(",")
    c = int(c)
    r = int(r)

    grid[r][c] = "#"

# 1024 definitely works (from pt. 1)
for i in range(1024, len(input)):
    c, r = input[i].split(",")
    c = int(c)
    r = int(r)

    grid[r][c] = "#"

    visited = {}

    bfs([(0, 0)], 0)

#    print(visited[(GRID_SIZE-1, GRID_SIZE-1)])
    if (GRID_SIZE-1, GRID_SIZE-1) not in visited.keys():
        print(f"{i}th bit has blocked the path!!!")
        print(c, r)
        break

    # print(input[i])
    # After every input:


def print_grid(grid, visited):
    g = copy.deepcopy(grid)

    for x, y in visited:
        g[x][y] = "•"
    for l in g:
        print("".join(l))


g = copy.deepcopy(grid)
for key, value in visited.items():
    x, y = key
    g[x][y] = str(value % 10)

for l in g:
    print("".join(l))



# for l in grid:
#     print("".join(l))

print(f"Time elapsed: {time.time() - start_time}s")
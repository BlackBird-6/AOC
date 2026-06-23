import random
import math
from itertools import *
from collections import *

import time

start_time = time.time()

input = open("inputs/2024_10.txt", "r+").read().splitlines()

total = 0

grid = [[c for c in r] for r in input]

NUM_ROWS = len(grid)
NUM_COLUMNS = len(grid[0])

order = "0 1 2 3 4 5 6 7 8 9".split()

for r in range(NUM_ROWS):
    for c in range(NUM_COLUMNS):
        grid[r][c] = int(grid[r][c])


def dfs(r, c):
    global total
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < NUM_ROWS and nc >= 0 and nc < NUM_COLUMNS:
            if grid[nr][nc] - grid[r][c] == 1:
                if grid[nr][nc] == 9:
                        total += 1
                else:
                    dfs(nr, nc)


roots = []
for r in range(NUM_ROWS):
    for c in range(NUM_COLUMNS):
        if grid[r][c] == 0:
            roots.append((r, c))

for r, c in roots:
    dfs(r, c)

for l in input:
    print(l)

print(total)

print(f"Time elapsed: {time.time() - start_time}s")

# import random
# import math
# from itertools import *
# from collections import *
#
# import time
# start_time = time.time()
#
# input = open("inputs/2024_10.txt", "r+").read().splitlines()
#
# total = 0
#
# grid = [[c for c in r] for r in input]
#
# NUM_ROWS = len(grid)
# NUM_COLUMNS = len(grid[0])
#
# order = "0 1 2 3 4 5 6 7 8 9".split()
#
#
# for r in range(NUM_ROWS):
#     for c in range(NUM_COLUMNS):
#         grid[r][c] = int(grid[r][c])
#
# def dfs(r, c):
#     global total
#     global seen
#     directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
#
#     for dr, dc in directions:
#         nr = r+dr
#         nc = c+dc
#         if nr >= 0 and nr < NUM_ROWS and nc >= 0 and nc < NUM_COLUMNS:
#             if grid[nr][nc] - grid[r][c] == 1:
#                 if grid[nr][nc] == 9:
#                     if (nr, nc) not in seen:
#                         seen.add((nr, nc))
#                         total += 1
#                 else:
#                     dfs(nr, nc)
#
#
#
# roots = []
# for r in range(NUM_ROWS):
#     for c in range(NUM_COLUMNS):
#             if grid[r][c] == 0:
#                 roots.append((r, c))
#
# for r, c in roots:
#     seen = set()
#     dfs(r, c)
#
#
#
# for l in input:
#     print(l)
#
# print(total)
#
# print(f"Time elapsed: {time.time() - start_time}s")
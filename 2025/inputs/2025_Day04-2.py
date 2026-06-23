import random
import math
from itertools import *
from collections import *
import numpy as np

import time # 16:42
start_time = time.time()

f = open("inputs/2025_04.txt", "r+").read().splitlines()

total = 0

grid = []
for l in f:
    grid.append([c for c in l])

adj = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
ROWS = len(grid)
COLUMNS = len(grid[0])
removals = []

while removals or total == 0:
    res = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    while removals:
        r, c = removals.pop()
        grid[r][c] = "."

    for r in range(ROWS):
        for c in range(COLUMNS):
            for dx, dy in adj:
                r2 = r+dx
                c2 = c+dy
                if(r2 < 0 or r2 >= ROWS or c2 < 0 or c2 >= COLUMNS):
                    continue
                if grid[r2][c2] == "@":
                    res[r][c] += 1
            if res[r][c] < 4 and grid[r][c] == "@":
                total += 1
                removals.append((r, c))

    # print("\033c", end="")
    # for l in grid:
    #     print("".join(l))
    # print("")

print(total)

print(f"Time elapsed: {time.time() - start_time}s") # 4.93s
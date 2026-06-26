import random
import math
from itertools import *
from collections import *

import time # 5:25
start_time = time.time()

f = open("inputs/2025_07.txt", "r+").read().splitlines()

total = 0
grid = []

for l in f:
    grid.append([c for c in l])

ROWS = len(grid)
COLS = len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if(grid[r][c] == "S" or grid[r][c] == "|" and r+1 != ROWS): # Beam goes down
            if grid[r+1][c] == "^":
                total += 1
                grid[r+1][c-1] = "|"
                grid[r+1][c+1] = "|"
            else:
                grid[r+1][c] = "|"

for l in grid:
    print("".join(l))
print(total)

print(f"Time elapsed: {time.time() - start_time}s")
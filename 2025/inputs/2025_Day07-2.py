import random
import math
from itertools import *
from collections import *

import time # 14:32
start_time = time.time()

f = open("inputs/2025_07.txt", "r+").read().splitlines()

total = 0
grid = []

for l in f:
    l = l.replace("S", "1")
    l = l.replace(".", "0")
    grid.append([c for c in l])

ROWS = len(grid)
COLS = len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] != "^":
            grid[r][c] = int(grid[r][c])

# grid[r][c] is the number of paths which enter (r,c)
for r in range(ROWS):
    for c in range(COLS):
        if(grid[r][c] != "^" and grid[r][c] != "." and r+1 != ROWS): # Beam goes down
            if grid[r+1][c] == "^":
                grid[r+1][c-1] += grid[r][c]
                grid[r+1][c+1] += grid[r][c]
            else:
                grid[r+1][c] += grid[r][c]
    
for l in grid:
    print((l))

print(sum(grid[-1]))

print(f"Time elapsed: {time.time() - start_time}s")
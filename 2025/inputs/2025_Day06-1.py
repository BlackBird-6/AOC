from itertools import accumulate
import random
import math
from itertools import *
from collections import *
import numpy as np

import time
start_time = time.time()

f = open("inputs/2025_06.txt", "r+").read().splitlines()

total = 0

grid = []
for l in f:
    grid.append(l.split())

grid = np.array(grid)
grid = np.transpose(grid)
grid = grid.tolist()
print(grid)

for l in grid:
    a, b, c, d = map(int, l[:4])
    if l[-1] == "+":
        total += a+b+c+d
    if l[-1] == "*":
        total += a*b*c*d

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
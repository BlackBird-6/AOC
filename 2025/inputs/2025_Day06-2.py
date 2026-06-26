from itertools import accumulate
import random
import math
from itertools import *
from collections import *
import numpy as np

import time # 29:19
start_time = time.time()

f = open("inputs/2025_06.txt", "r+").read().splitlines()

total = 0

grid = []
stack = []

for l in f:
    grid.append([c for c in l])

grid = np.array(grid)
grid = np.transpose(grid)
grid = grid.tolist()

print(grid)

operation = "*"

for row in grid: # ['1', '0', '0', '*']
    print(row)
    if row[-1] == "*":
        operation = "*"
    elif row[-1] == "+":
        operation = "+"
    
    if all([row[i] == " " for i in range(len(row)-1)]):
        res = stack.pop()
        while stack:
            if operation == "*":
                res *= stack.pop()
            else:
                res += stack.pop()
        total += res
        print(res)
    else:
        stack.append(int("".join(row[:-1])))
print(total)

print(f"Time elapsed: {time.time() - start_time}s")
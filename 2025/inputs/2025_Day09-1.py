import random
import math
from itertools import *
from collections import *

import time # 3:30
start_time = time.time()

f = open("inputs/2025_09.txt", "r+").read().splitlines()

res = 0

tiles = []
for l in f:
    x, y = l.split(",")
    tiles.append((int(x), int(y)))

for t1 in tiles: # brute force 
    for t2 in tiles:
        res = max(res, abs(t1[0] - t2[0] + 1) * abs(t1[1] - t2[1] + 1))
print(res)

print(f"Time elapsed: {time.time() - start_time}s")
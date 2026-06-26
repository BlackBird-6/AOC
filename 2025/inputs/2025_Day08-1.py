from math import sqrt
import random
import math
from itertools import *
from collections import *

import time # 31:57
start_time = time.time()

f = open("inputs/2025_08.txt", "r+").read().splitlines()

NUM_CONNECTIONS = 1000
total = 0

boxes = [] # Part 1: parse input
for l in f:
    x, y, z = l.split(",")
    x, y, z = map(int, (x, y, z))
    boxes.append((x, y, z))

distances = [] # Part 2: find all box distance pairs
for i, b1 in enumerate(boxes):
    for b2 in boxes[i+1:]:
        distances.append((math.dist(b1, b2), b1, b2))
distances.sort()

adjs = defaultdict(list) # Part 3: Build adjacency list
for i in range(NUM_CONNECTIONS):
    n1, n2 = distances[i][1], distances[i][2]
    adjs[n1].append(n2)
    adjs[n2].append(n1)

res = [] # Part 4: Find sizes of all circuits
visited = set()
for node in boxes:

    if node in visited:
        continue
    
    size = 0
    targets = [node]
    while targets:
        next_node = targets.pop(0)
        if next_node in visited:
            continue
        visited.add(next_node)
        size += 1
        for nei in adjs[next_node]:
            targets.append(nei)
    res.append((size, node))

res.sort()
print(res)
print(res[-1][0] * res[-2][0] * res[-3][0])

print(f"Time elapsed: {time.time() - start_time}s") # 0.61s
from math import sqrt
import random
import math
from itertools import *
from collections import *

import time # 54:52
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

def trial(N):
    adjs = defaultdict(list) # Part 3: Build adjacency list
    for i in range(N):
        n1, n2 = distances[i][1], distances[i][2]
        adjs[n1].append(n2)
        adjs[n2].append(n1)

    res = [] # Part 4: Find sizes of all circuits
    visited = set()

    size = 0
    targets = [boxes[0]]
    while targets:
        next_node = targets.pop(0)
        if next_node in visited:
            continue
        visited.add(next_node)
        size += 1
        for nei in adjs[next_node]:
            targets.append(nei)
    
    return size == len(boxes)
    
low = 0
high = len(boxes)*len(boxes)/2

while low < high:
    par = math.floor((low+high)/2)
    print(low, high, par)
    if trial(par):
        high = par
    else:
        low = par+1

print(low, high)

for i, l in enumerate(distances):
    if i == par:
        print(i+1, l)
    

print(f"Time elapsed: {time.time() - start_time}s") # 244.96s

# 1: A
# 2: B
# 1: C
# A-C
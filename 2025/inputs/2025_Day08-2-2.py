from math import sqrt
import random
import math
from itertools import *
from collections import *

import time
start_time = time.time()

f = open("inputs/2025_08.txt", "r+").read().splitlines()

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

res = {} # Part 3: The rest
components = len(boxes)
for b in boxes:
    res[b] = b

def find(n):
    while(res[n] != n):
        res[n] = res[res[n]]
        n = res[n]
    return n

def union(n1, n2):
    global components
    f1, f2 = find(n1), find(n2)
    if f1 == f2:
        return
    res[f1] = f2
    components -= 1

for i in range(10**9):
    n1, n2 = distances[i][1], distances[i][2]
    union(n1, n2)
    if components == 1:
        print(n1, n2)
        break

print(f"Time elapsed: {time.time() - start_time}s") # 0.78s
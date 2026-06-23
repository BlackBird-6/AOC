import random
import math
from itertools import *
from collections import *

import time
start_time = time.time()

input = open("inputs/2024_25.txt", "r+").read().split("\n\n")

total = 0

locks = []
# 0 5 3 4 3

keys = []
for l in input:
    l = l.splitlines()

    lock = [-1, -1, -1, -1, -1]


    # Lock
    if(l[0] == "#####"):
        for row in l:
            print(lock)
            print(row)
            for i in range(5):
                if row[i] == "#":
                    lock[i] += 1
        locks.append(lock)

    # Key
    if (l[0] == "....."):
        for row in l:
            for i in range(5):
                if row[i] == "#":
                    lock[i] += 1
        for n in lock:
            n = 7-n
        keys.append(lock)

    print(l)

print(locks, keys)
for k in keys:
    k1, k2, k3, k4, k5 = k
    for l in locks:
        l1, l2, l3, l4, l5 = l
        if k1+l1 <= 5 and k2+l2 <= 5 and k3+l3 <= 5 and k4+l4 <= 5 and k5+l5 <= 5:
            total += 1
            print(k, l)

print(total)
print(f"Time elapsed: {time.time() - start_time}s")
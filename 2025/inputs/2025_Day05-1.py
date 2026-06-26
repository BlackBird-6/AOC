from _winapi import STD_OUTPUT_HANDLE
import random
import math
from itertools import *
from collections import *

import time
start_time = time.time()

f = open("inputs/2025_05.txt", "r+").read().splitlines()

total = 0

ranges = []
targets = []
MODE = "in"
for l in f:

    if l == "":
        MODE = "out"
        continue

    if MODE == "in":
        l = l.split("-")
        ranges.append((int(l[0]), int(l[1])))
       
    if MODE == "out":
        targets.append(int(l))
     
print(ranges)
print(targets)
for n in targets:
    for l, h in ranges:
        if n >= l and n <= h:
            total += 1
            break

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
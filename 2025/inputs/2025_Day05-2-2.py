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
new_ranges = []

for l in f:

    if l == "":
        break

    l = l.split("-")
    ranges.append((int(l[0]), int(l[1])))

ranges.sort()

l, h = ranges[0]

for l2, h2 in ranges[1:]:
    print(l, h)
    if l2 <= h+1:
        h = max(h, h2)
    else:
        total += h-l+1
        l, h = l2, h2    

total += h-l+1

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
from _winapi import STD_OUTPUT_HANDLE
import random
import math
from itertools import *
from collections import *

import time # 54:13
start_time = time.time()

f = open("inputs/2025_05.txt", "r+").read().splitlines()

total = 0

ranges = []
new_ranges = []

for l in f:

    if l == "":
        break

    l = l.split("-")
    ranges.append((int(l[0]), "L"))
    ranges.append((int(l[1])+1, "H"))

ranges.sort(key=lambda s: s[0])
print(ranges)

low = 0
tally = 0
while ranges:
    n, bound = ranges.pop(0)
    print(n, bound, tally)
    if bound == "L":
        if tally == 0:
            low = n
        tally += 1
    else:
        tally -= 1
        if tally == 0:
            new_ranges.append((low, n))

print(new_ranges)


for l, h in new_ranges:
    total += h - l 

print(total)

print(f"Time elapsed: {time.time() - start_time}s")

# for l in f:

#     if l == "":
#         break

#     l = l.split("-")
#     ranges.append((int(l[0]), int(l[1])))
            
# # for l, h in ranges:

#     to_remove = []
#     for l2, h2 in new_ranges: # 1 compared against 2 (existing)

#         if l <= l2 and h >= h2: # New completely encapsulates existing range, delete old one
#             to_remove.append((l2, h2))
    
#     while to_remove:
#         new_ranges.remove(to_remove.pop())
            
#     for l2, h2 in new_ranges:
#         if l >= l2 and h <= h2: # Is completely encapsulated, delete this one
#             l = -99
#             h = -100 
        
#         if l >= l2 and l <= h2 and h > h2:
#             l = h2+1
        
#         if l < l2 and h >= l2 and h <= h2:
#             h = l2-1
        
#     new_ranges.append((l, h))
#     print(new_ranges)

import random
import math
from itertools import *
from collections import *

import time # 5:20
start_time = time.time()

input = open("inputs/2025_01.txt", "r+").read().splitlines()

current = 50
total = 0

for l in input:
    mult = 1 if l[0] == "R" else -1
    
    for i in range(int(l[1:])): # brute force solution (sum of terms is 597303)
        current += mult
        current = current % 100

        if current == 0:
            total += 1

print(total)

# 1200
# 833
# 640

print(f"Time elapsed: {time.time() - start_time}s")
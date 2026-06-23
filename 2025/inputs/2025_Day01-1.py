import random
import math
from itertools import *
from collections import *

import time # 3:27
start_time = time.time()

input = open("inputs/2025_01.txt", "r+").read().splitlines()

current = 50
total = 0

for l in input:
    mult = 1 if l[0] == "R" else -1
    current += mult * int(l[1:])
    current = current % 100

    print(l, current)
    if current == 0:
        total += 1

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
from importlib import readers
import random
import math
from itertools import *
from collections import *

import time # 10:35
start_time = time.time()

input = open("inputs/2025_02.txt", "r+").read().splitlines()

total = 0

for l in input:
    ranges = [(low, high) for low, high in (s.split("-") for s in l.split(","))]
    # print(ranges)
    # print(sum([(int(high) - int(low)) for low, high in ranges])) # 2.5M

    for low, high in ranges:
        for i in range(int(low), int(high)+1):
            check = str(i)
            half = int(len(check)/2)

            if len(check) % 2 != 0:
                continue
            # 6, 0-3 3-5
            # print(check)
            # print(check[:half], check[half:])

            if check[:half] == check[half:]:
                total += int(check)
    print(total)

print(f"Time elapsed: {time.time() - start_time}s")
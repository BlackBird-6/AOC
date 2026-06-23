import random
import math
from itertools import *
from collections import *

import time # 8:22
start_time = time.time()

f = open("inputs/2025_03.txt", "r+").read().splitlines()


# 811111111111119

total = 0
# two pass, scan for the leftmost largest digit anywhere but the final digit of the code
# then scan for the largest digit right of that, then combine
for l in f:
    tens = 0
    ones = 0
    for i in range(len(l)):
        n = int(l[i])
        
        if n > tens and i != len(l)-1:
            tens = n
            ones = 0
            continue
        
        if n > ones:
            ones = n

    total += 10*tens + ones

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
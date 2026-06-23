import random
import math
from itertools import *
from collections import *

import time # 26:41
start_time = time.time()

f = open("inputs/2025_03.txt", "r+").read().splitlines()

# one pass O(n), scan for the kth largest digit anywhere but the final digit(s) of the code
# and zero out all future values when seen
total = 0
for l in f:
    largest = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l)):
        n = int(l[i])
        
        for k in range(len(largest)):
            if n > largest[k] and i <= len(l) - (len(largest)-k): # 11112222339990000 len=17 k=7 (4th last) <= 13 = len(l) - len(largest) - k
                largest[k] = n
                for j in range(k+1, len(largest)):
                    largest[j] = 0
                break

    # print(int("".join([str(n) for n in largest]))) 
    total += int("".join([str(n) for n in largest]))

print(total)

print(f"Time elapsed: {time.time() - start_time}s") # 0.095s

# 313021889619
# 3121910778619
# 3121910778619

# 932835543135333462635233343534
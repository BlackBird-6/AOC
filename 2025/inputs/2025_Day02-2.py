from importlib import readers
import random
import math
from itertools import *
from collections import *

import time # 35:13
start_time = time.time()

input = open("inputs/2025_02.txt", "r+").read().splitlines()

total = set() # numbers like 222222 are picked up twice
PRIMES = [2, 3, 5, 7, 11]
for l in input:
    ranges = [(low, high) for low, high in (s.split("-") for s in l.split(","))]

    for low, high in ranges:
        for i in range(int(low), int(high)+1):
            check = str(i)
            for p in PRIMES: # nonprime repeats will also repeat on their prime factors
                
                if len(check) % p != 0:
                    continue

                partitions = range(0, len(check)+1, int(len(check)/p))  # 9: 0-3 3-6 6-9

                invalidID = True
                for i in range(1, len(partitions)-1):
                    if check[partitions[i-1]:partitions[i]] != check[partitions[i]:partitions[i+1]]:
                        invalidID = False
                        break

                if invalidID:
                    total.add(int(check)) 
                    break
            
    print(sum(total))

print(f"Time elapsed: {time.time() - start_time}s") # 7.1s
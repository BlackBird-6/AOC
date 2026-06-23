import random
import math
from itertools import *
from collections import *

import time
start_time = time.time()

input = open("inputs/2024_11.txt", "r+").read().splitlines()

total = 0

pre_stones = [int(n) for n in input[0].split()]
stones = Counter(pre_stones)



# 0(75) --> 1(74) --> 2024(73) --> 20(72) 24(72) --> 2(71) 0(71) 2(71) 4(71)
# 0 --> 1 --> 2024 --> 20 24 --> 2 0 2 4 --> 4048 1 4048 8096 ...

for k in range(75):
    print(k, len(stones))

    new_stones = defaultdict(int)
    for number, count in stones.items():


        if number == 0:
            new_stones[1] += count

        elif len(str(number)) % 2 == 0:
            num = str(number)
            # 012345

            partition = int(len(num)/2)
            n1, n2 = num[:partition], num[partition:]

            new_stones[int(n1)] += count
            new_stones[int(n2)] += count
        else:
            new_stones[number*2024] += count

    stones = new_stones

print(stones)
for val in stones.values():
    total += val
print(total)
print(len(stones.values()))


print(f"Time elapsed: {time.time() - start_time}s")
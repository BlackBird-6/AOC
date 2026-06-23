import math
import random
import typing
import re
from itertools import *
from collections import *
import time
start_time = time.time()

input = open("inputs/2024_22.txt", "r+").read().splitlines()

total = 0


# sequence = [-2, 1, -1, 3]

totals = defaultdict(int)

for i, n in enumerate(input):

    print(f"{i}/{len(input)}")

    n = int(n)

    last = n % 10
    changes = []
    seen = set()

    for i in range(2000):

        n = n^(n*64)
        n = n % 16777216
        n = n ^ (math.floor(n/32))
        n = n % 16777216
        n = n ^ (n * 2048)
        n = n % 16777216

        if len(changes) >= 4:
            comb = (changes[0], changes[1], changes[2], changes[3])
            if comb not in seen:
                totals[comb] += last
            seen.add(comb)
            changes.pop(0)

        changes.append((n % 10) - last)
        last = n % 10

print(totals)
print(max(totals.values()))


print(f"Time elapsed: {time.time() - start_time}s")
# Without set: 30.1507s
# With set: 2.4420s

# import math
# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_22.txt", "r+").read().splitlines()
#
# total = 0
#
# # input = [1, 10, 100, 2024]
#
#
# for n in input:
#     n = int(n)
#     for i in range(2000):
#
#         n = n^(n*64)
#         n = n % 16777216
#         n = n ^ (math.floor(n/32))
#         n = n % 16777216
#         n = n ^ (n * 2048)
#         n = n % 16777216
#
#     total += n
#
# print(total)
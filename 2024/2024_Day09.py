import random
import math
from itertools import *
from collections import *

import time

start_time = time.time()

input = open("inputs/2024_09.txt", "r+").read().splitlines()

total = 0

disk = []

for l in input:
    for i, n in enumerate(l):
        n = int(n)
        if i % 2 == 0:
            disk += [[i / 2, n]]
        else:
            disk += [[-1, n]]
    print(len(l))
    print(l)


# R iterates through files
R = len(disk) - 1

# Find file space of next file
while R > 0:
    if disk[R][0] != -1 and disk[R][1] > 0:
        file_space = disk[R][1]

        L = 1
        while L < R:
            if disk[L][0] == -1:

                # print(disk[L][1], file_space)
                if disk[L][1] >= file_space:
                    disk[L][1] -= file_space
                    s = disk[R][0]
                    disk[R] = [-1, file_space]
                    disk.insert(L, [s, file_space])
                    # New term added, so move indices by one
                    R += 1
                    break

            # L iterates through empty space
            L += 1
    R -= 1

new_disk = []
for n, count in disk:
    new_disk += [n] * count

print(new_disk)

for i, n in enumerate(new_disk):
    if n != -1:
        total += i * n

print(total)

print(f"Time elapsed: {time.time() - start_time}s")

# import random
# import math
# from itertools import *
# from collections import *
#
# import time
# start_time = time.time()
#
# input = open("inputs/2024_09.txt", "r+").read().splitlines()
#
# total = 0
#
# disk = []
#
# for l in input:
#     for i, n in enumerate(l):
#         n = int(n)
#         if i % 2 == 0:
#             disk += [i/2]*n
#         else:
#             disk += [-1]*n
#     print(len(l))
#     print(l)
#
# L = 0
# R = len(disk)-1
#
# while L < R:
#
#     if disk[L] == -1 and disk[R] != -1:
#         disk[L], disk[R] = disk[R], disk[L]
#
#     if disk[L] != -1:
#         L += 1
#
#     if disk[R] == -1:
#         R -= 1
#
# for i, n in enumerate(disk):
#     if n != -1:
#         total += i*n
# print(total)
#
#
# print(f"Time elapsed: {time.time() - start_time}s")
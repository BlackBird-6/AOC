import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2024_02.txt", "r+").read().splitlines()

total = 0

for l in input:
    nums_full = l.split()

    for k in range(len(nums_full)):

        safe = True
        all_inc = True
        all_dec = True
        nums = nums_full.copy()
        nums.pop(k)
        print(nums)

        for i in range(len(nums) - 1):
            a, b = int(nums[i]), int(nums[i + 1])
            if a >= b:
                all_inc = False
            if a <= b:
                all_dec = False
            dist = abs(a - b)
            if dist < 1 or dist > 3:
                safe = False
                break
        if all_inc == False and all_dec == False:
            safe = False

        if safe == True:
            total += 1
            break

print(total)

# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_02.txt", "r+").read().splitlines()
#
# total = 0
#
# for l in input:
#     nums = l.split()
#     safe = True
#     all_inc = True
#     all_dec = True
#
#     for i in range(len(nums)-1):
#         a, b = int(nums[i]), int(nums[i+1])
#         if a >= b:
#             all_inc = False
#         if a <= b:
#             all_dec = False
#         dist = abs(a - b)
#         if dist < 1 or dist > 3:
#             safe = False
#             break
#     if all_inc == False and all_dec == False:
#         safe = False
#     total += safe
#
# print(total)
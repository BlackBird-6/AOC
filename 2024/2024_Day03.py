import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2024_03.txt", "r+").read().splitlines()

total = 0

enable = 1

for l in input:
    results = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", l)
    for r in results:
        print(r)

        if r == "do()":
            enable = 1
        elif r == "don't()":
            enable = 0
        else:
            nums = re.findall("(\d+),(\d+)", r)
            total += int(nums[0][0]) * int(nums[0][1]) * enable

print(total)

# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_03.txt", "r+").read().splitlines()
#
# total = 0
#
# for l in input:
#     results = re.findall("mul\(\d+,\d+\)", l)
#
#     for r in results:
#         nums = re.findall("(\d+),(\d+)", r)
#         total += int(nums[0][0]) * int(nums[0][1])
#
# print(total)
import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_04.txt", "r+").read().splitlines()

total = 0

cards = [1 for line in input]

print(cards)

for i, line in enumerate(input):
    line = line.split("|")

    winning = line[0].split()[2:]
    numbers = line[1].split()

    count = 0
    for w in winning:
        for n in numbers:
            if w == n:
                count += 1

    print(count, "matches on card", i)

    for j in range(i+1, i+1+count):
        cards[j] += 1*cards[i]
    print(cards)


for e in cards:
    total += e
print(total)


# 2 (1)
# 2
# 2
# 2

# Part 1
# input = open("inputs/2023_04.txt", "r+").read().splitlines()
#
# total = 0
#
# for line in input:
#     line = line.split("|")
#     print(line)
#     winning = line[0].split()[2:]
#     numbers = line[1].split()
#     print(winning)
#     print(numbers)
#
#     score = 0
#     for w in winning:
#         for n in numbers:
#             if w == n:
#                 print(n)
#                 if score == 0:
#                     score = 1
#                 else:
#                     score *= 2
#     total += score
# print(total)
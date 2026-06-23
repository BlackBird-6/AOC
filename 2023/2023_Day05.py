import random
import typing
import re
from itertools import *
from collections import *
import time

# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48

input = open("inputs/2023_05.txt", "r+").read().splitlines()

pre_seeds = re.findall("\d+", input[0])
pre_seeds = list(map(int, pre_seeds))
print(pre_seeds)

# The seed number should be 1392140761 within a margin of 200,000.
# pre_seeds = [961540761, 489996751]
# pre_seeds = [1392140761, 200000]
pre_seeds = [1392045551, 100]

# 1392045591 within a margin of... 2

# The correct answer is 2520470~2520480

seeds = []

for i in range(0, len(pre_seeds), 2):
    seeds.append(pre_seeds[i])
    for k in range(0, pre_seeds[i+1], 1):
        # if(abs(pre_seeds[i]+k - 1392140761) < 200000):
        #     print(pre_seeds[i], pre_seeds[i+1])

        seeds.append(pre_seeds[i]+k)
    # seeds.append(pre_seeds[i]+pre_seeds[i+1])
# seeds = [100000*i for i in range(10000)]
print("Current Seeds", seeds)

maps = []
set = []

# Generate list of map "rules"
for l in input[2:]:

    if not l:
        maps.append(set)
        set = []
    else:
        if not l.endswith(":"):
            set.append(l)

# Convert seed through ruleset
for i in range (len(seeds)):
    temp = seeds[i]
    seeds[i] = int(seeds[i])
    for set in maps:
            for rule in set:

                rule = rule.split()
                rule = list(map(int, rule))

                # print(rule)
                # print(seed,rule[1],rule[1] + rule[2])

                if(rule[1] <= seeds[i] and seeds[i] <= rule[1] + rule[2]):

                    # print("Before",seed)
                    seeds[i] += rule[0]-rule[1]
                    # print("After",seed)
                    # print(seeds)
                    break

    # 2615650 is the location number that comes from trials of 10,000 spaced apart (note that all ranges span across over one million)
    # if(seeds[i] == 2520480):
    #     print(f"{temp} is the winning seed number!")
        # This is 1392140761
        # Is in the bounds 961540761, 489996751

print("Seeds:",seeds)

print(min(seeds))
    # 50 98 2, 52 50 48


# Part 1
# input = open("inputs/2023_05.txt", "r+").read().splitlines()
#
# seeds = re.findall("\d+", input[0])
# print(seeds)
#
# maps = []
# set = []
#
# # Generate list of map "rules"
# for l in input[2:]:
#
#     if not l:
#         maps.append(set)
#         set = []
#     else:
#         if not l.endswith(":"):
#             set.append(l)
#
# # Convert seed through ruleset
# for i in range (len(seeds)):
#     seeds[i] = int(seeds[i])
#     for set in maps:
#             for rule in set:
#
#                 rule = rule.split()
#                 rule = list(map(int, rule))
#
#                 print(rule)
#                 # print(seed,rule[1],rule[1] + rule[2])
#
#                 if(rule[1] <= seeds[i] and seeds[i] <= rule[1] + rule[2]):
#
#                     # print("Before",seed)
#                     seeds[i] += rule[0]-rule[1]
#                     # print("After",seed)
#                     print(seeds)
#                     break
#
#
# print("Seeds:",seeds)
#
# print(min(seeds))
#     # 50 98 2, 52 50 48



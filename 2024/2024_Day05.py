import random
import typing
import re
from itertools import *
from collections import *
import math

input = open("inputs/2024_05.txt", "r+").read().splitlines()

total = 0

rules = []
sequences = []

for l in input:
    if "|" in l:
        l = l.split("|")
        rules.append([l[0], l[1]])
    if "," in l:
        sequences.append(l.split(","))

print(rules)

for sequence in sequences:
    follows_rules = True

    for r1, r2 in rules:
        if r1 in sequence and r2 in sequence:
            for num in sequence:
                if num == r1:
                    break
                if num == r2:
                    follows_rules = False
                    break

    # sort it if unsorted
    if follows_rules == False:

        # Repeat len(sequence times)
        print(sequence)

        for k in range(len(sequence)):

            # Insertion sort
            for r1, r2 in rules:
                if r1 in sequence and r2 in sequence:
                    i, j = -1, -1
                    for k, num in enumerate(sequence):
                        if num == r1:
                            i = k
                        if num == r2:
                            j = k
                    if j < i:
                        sequence[i], sequence[j] = sequence[j], sequence[i]

        print(sequence)
        middle = int(sequence[math.floor(len(sequence) / 2)])
        print(middle)
        total += middle

print(total)

# import random
# import typing
# import re
# from itertools import *
# from collections import *
# import math
#
# input = open("inputs/2024_05.txt", "r+").read().splitlines()
#
# total = 0
#
# rules = []
# sequences = []
#
# for l in input:
#     if "|" in l:
#         l = l.split("|")
#         rules.append([l[0], l[1]])
#     if "," in l:
#         sequences.append(l.split(","))
#     print(l)
#
# for sequence in sequences:
#     follows_rules = True
#     for r1, r2 in rules:
#         if r1 in sequence and r2 in sequence:
#             for num in sequence:
#                 if num == r1:
#                     break
#                 if num == r2:
#                     follows_rules = False
#                     break
#     if follows_rules == True:
#         middle = int(sequence[math.floor(len(sequence)/2)])
#         print(middle)
#         total += middle
#
# print(rules)
# print(sequences)
# print(total)
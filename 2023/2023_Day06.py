import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_06.txt", "r+").read().splitlines()

total = 0

times_pre = re.findall("\d+", input[0])
dists_pre = re.findall("\d+", input[1])

t_list = []
d_list = []

times = ""
dists = ""

for i in range(len(times_pre)):
    t_list.append(times_pre[i])
    d_list.append(dists_pre[i])

t = int("".join(t_list))
d = int("".join(d_list))

count = 0
for j in range(t):
    if j*(t-j) > d:
        count += 1

print(count)


# input = open("inputs/2023_06.txt", "r+").read().splitlines()
#
# total = 0
#
# times = list(map(int, re.findall("\d+%", input[0])))
# dists = list(map(int, re.findall("\d+%", input[1])))
#
# product = 1
#
# for i, t in enumerate(times):
#
#     count = 0
#     for j in range(t):
#         if j*(t-j) > dists[i]:
#             print(j, t-j)
#             count += 1
#
#     print(count)
#     product *= count
#
# print(product)

import random
import typing
import re
from itertools import *
from collections import *
import time
start_time = time.time()

input = open("inputs/2024_23.txt", "r+").read().splitlines()

total = 0

g = defaultdict(list)

for l in input:
    A, B = l.split("-")
    g[A].append(B)
    g[B].append(A)

res = []

visited = []

# res = ['ku', 'xj', 'sh', 'ps', 'ty', 'qq', 'xi', 'hl', 'io', 'wq', 'yp', 'pk', 'tx']
#
# res = sorted(res)
# print(",".join(r for r in res))

for node in g.keys():
    largest = []
    largest.append(node)

    for nei in g[node]:

        if nei in largest:
            continue

        appears_in_all = True
        for other_nodes in largest:
            if nei not in g[other_nodes]:
                appears_in_all = False
                break
        if appears_in_all == True:
            largest.append(nei)

    print(largest)
    if len(largest) > len(res):
        res = largest

print(",".join(r for r in sorted(res)))

print(f"Time elapsed: {time.time() - start_time}s")

# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_23.txt", "r+").read().splitlines()
#
# total = 0
#
# g = defaultdict(list)
#
# for l in input:
#     A, B = l.split("-")
#     g[A].append(B)
#     g[B].append(A)
#
# res = []
#
# visited = []
# for node in g.keys():
#     for nei in g[node]:
#         for a in g[node]:
#             if a in g[nei]:
#                 comb = sorted([node, nei, a])
#                 if comb not in res:
#                     res.append(comb)
#
# res2 = []
# for comb in res:
#     if comb[0][0] == "t" or comb[1][0] == "t" or comb[2][0] == "t":
#         res2.append(comb)
# print(res2)
# print(len(res2))
# print(g)
import random
import time
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_08.txt", "r+").read().splitlines()

total = 0

graph = defaultdict(list)
# NBN -> (BKF, NNH) [0] [1]

primes = [2]
for i in range(3, 10000, 2):
    divides = True
    for p in primes:
        if i % p == 0:
            divides = False
            break
    if divides == True:
        primes.append(i)


def lcm(n1, n2):
    n1_factors = []
    n2_factors = []
    for p in primes:
        while n1 % p == 0:
            n1_factors.append(p)
            n1 /= p
        while n2 % p == 0:
            n2_factors.append(p)
            n2 /= p

    print(n1_factors, n2_factors)
    for f1 in n1_factors:
        if f1 in n2_factors:
            n2_factors.remove(f1)
    print(n1_factors, n2_factors)
    res = 1

    for p in n1_factors + n2_factors:
        res *= p

    return(res)

direction = input[0]
print(direction)

for line in input[2:]:
    a, b, c = re.findall("\w\w\w", line)
    print(a, b, c)
    graph[a] = (b, c)
    print(line)

locations = []
for key in graph.keys():
    if key[-1] == "A":
        locations.append(key)

results = [0, 0, 0, 0, 0, 0]

while True:
    for char in direction:
        for i in range(len(locations)):
            if char == "L":
                locations[i] = graph[locations[i]][0]
            else:
                locations[i] = graph[locations[i]][1]


        total += 1
        print(locations)

        for i in range(len(locations)):
            if locations[i][-1] == "Z":
                if results[i] == 0:
                    results[i] = total


        if 0 not in results:
            print(results)

            res = 1
            for r in results:
                res = lcm(res, r)
                print(res)
            time.sleep(15)





# input = open("inputs/2023_08.txt", "r+").read().splitlines()
#
# total = 0
#
# graph = defaultdict(list)
# # NBN -> (BKF, NNH) [0] [1]
#
# direction = input[0]
# print(direction)
#
# for line in input[2:]:
#     a, b, c = re.findall("\w\w\w", line)
#     print(a, b, c)
#     graph[a] = (b, c)
#     print(line)
#
# location = "AAA"
# while True:
#     for char in direction:
#         if char == "L":
#             location = graph[location][0]
#         else:
#             location = graph[location][1]
#
#         print(location)
#         total += 1
#         if location == "ZZZ":
#             print(total)
#             time.sleep(10)
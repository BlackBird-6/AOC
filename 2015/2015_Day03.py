import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_03.txt", "r+").read()

total = 0
turn = 0
x1 = 1000
y1 = 1000
x2 = 1000
y2 = 1000

arr = [[[0] for i in range (2000)] for j in range (2000)]


print(arr[1000][1000][0])

for char in input:

    if turn % 2 == 0:
        if char == "v":
            y1 -= 1
        if char == "^":
            y1 += 1
        if char == "<":
            x1 -= 1
        if char == ">":
            x1 += 1
        arr[x1][y1][0] += 1

    else:
        if char == "v":
            y2 -= 1
        if char == "^":
            y2 += 1
        if char == "<":
            x2 -= 1
        if char == ">":
            x2 += 1
        arr[x2][y2][0] += 1

    turn += 1

for i in range (len(arr)):
    for j in range (len(arr[0])):
        if arr[i][j][0] >= 1:
            total += 1
print(total)

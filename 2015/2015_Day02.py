import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_02.txt", "r+")

total = 0
for line in input:

    w, l, h = line.replace("\n","").split("x")
    w, l, h = int(w), int(l), int(h)

    total += 2*(min(w+l, w+h, l+h)) + w*l*h
    # total += 2*(dims[0]*dims[1] + dims[0]*dims[2] + dims[1]*dims[2]) + min(dims[0], dims[1], dims[2])
    print(total)



  # dims = line.replace("\n","").split("x")
    # w = int(dims[0])
    # l = int(dims[1])
    # h = int(dims[2])


#     Part 1
#     input = open("inputs/2015_02.txt", "r+")
#
# total = 0
# for line in input:
#     dims = line.replace("\n","").split("x")
#     w = int(dims[0])
#     l = int(dims[1])
#     h = int(dims[2])
#
#     total += 2*(w*l + l*h + w*h) + min(w*l, l*h, w*h)
#     # total += 2*(dims[0]*dims[1] + dims[0]*dims[2] + dims[1]*dims[2]) + min(dims[0], dims[1], dims[2])
#     print(total)

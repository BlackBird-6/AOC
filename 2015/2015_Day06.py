import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_06.txt", "r+").read().splitlines()
total = 0
size = 1000
count = 0

lights = [[0 for i in range (size)] for i in range (size)]

def interpret(type, bound1x, bound1y, bound2x, bound2y):
    # All on
    if type == 0:
        for i in range(bound1x, bound2x+1):
            for j in range(bound1y, bound2y+1):
                lights[i][j] += 1
    # All off
    if type == 1:
        for i in range(bound1x, bound2x+1):
            for j in range(bound1y, bound2y+1):
                if (lights[i][j] > 0):
                    lights[i][j] -= 1

    # Toggle
    if type == 2:
        for i in range(bound1x, bound2x+1):
            for j in range(bound1y, bound2y+1):
                lights[i][j] += 2

for line in input:
    mode = 0
    if "turn on" in line:
        mode = 0
    elif "turn off" in line:
        mode = 1
    else:
        mode = 2

    # print(line)

    line = re.findall("[1234567890]+", line)


    # print(mode, int(line[0]), int(line[1]), int(line[2]), int(line[3]))

    interpret(mode, int(line[0]), int(line[1]), int(line[2]), int(line[3]))


for a in lights:
    print(a)

for a in lights:
    for b in a:
        count += b

print(count)

# def interpret(type, bound1x, bound1y, bound2x, bound2y):
#     # All on
#     if type == 0:
#         for i in range(bound1x, bound2x+1):
#             for j in range(bound1y, bound2y+1):
#                 lights[i][j] = 1
#     # All off
#     if type == 1:
#         for i in range(bound1x, bound2x+1):
#             for j in range(bound1y, bound2y+1):
#                 lights[i][j] = 0
#
#     # Toggle
#     if type == 2:
#         for i in range(bound1x, bound2x+1):
#             for j in range(bound1y, bound2y+1):
#                 if lights[i][j] == 0:
#                     lights[i][j] = 1
#                 else:
#                     lights[i][j] = 0
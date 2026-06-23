import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_02.txt", "r+")

count = 0
total = 0
red = 12
green = 13
blue = 14

for line in input:
    red = 0
    green = 0
    blue = 0

    line = line.replace("\n","")
    line = line.split()
    line = line[::-1]

    print(line)
    for i in range(0, len(line)-2, 2):
        new = int(line[i+1])

        if "red" in line[i] and red < new:
            red = new
        if "green" in line[i] and green < new:
            green = new
        if "blue" in line[i] and blue < new:
            blue = new

    print(red, green, blue)
    total += red * green * blue






print(total)

#         if "red" in line[i] and int(line[i+1]) <= red:
#             a = 1
#         elif "green" in line[i] and int(line[i+1]) <= green:
#             a = 1
#         elif "blue" in line[i] and int(line[i+1]) <= blue:
#             a = 1
#         elif line[i+1] == "Game":
#             print("VALID")
#             total += count
#             print(total)
#         else:
#             print("### INVALID")
#             break
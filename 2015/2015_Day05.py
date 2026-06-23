import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_05.txt", "r+").read().splitlines()

total = 0



vowels = "aeiou"

for line in input:
    print(line)
    lastchar = ""
    req1 = 0
    req2 = 0
    nice = True

    for i in range(len(line)):
        try:
            if(line[i] == line[i+2]):
                req1 = 1

            if(line[i:i+2] in line[i+2:]):
                req2 = 1
        except:
            {}


    if req1 >= 1 and req2 >= 1:
        total += 1
        print("Nice")

print(total)

# for line in input:
#     lastchar = ""
#     vowelcount = 0
#     doublecount = False
#     nice = True
#
#     for char in line:
#         if char in vowels:
#             vowelcount += 1
#         if char == lastchar:
#             doublecount = True
#         lastchar = char
#
#     if vowelcount < 3:
#         nice = False
#
#     if doublecount == False:
#         nice = False
#
#     if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
#         nice = False
#
#     if nice == True:
#         print(line)
#         total += 1
#
# print(total)

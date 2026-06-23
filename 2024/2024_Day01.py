import random
import time
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2024_01.txt", "r+").read().splitlines()

n1 = []
n2 = []

for l in input:
    num1, num2 = l.split()
    n1.append(int(num1))
    n2.append(int(num2))
n1.sort()
n2.sort()

n2_count = Counter(n2)
total = 0

for i in range(len(n1)):
    total += n1[i] * n2_count[n1[i]]

print(total)

# input = open("inputs/2024_01.txt", "r+").read().splitlines()
#
# n1 = []
# n2 = []
#
# for l in input:
#     num1, num2 = l.split()
#     n1.append(int(num1))
#     n2.append(int(num2))
# n1.sort()
# n2.sort()
#
# total = 0
#
# for i in range(len(n1)):
#     total += (abs(n2[i] - n1[i]))
#     print(n2[i], n1[i])
#
# print(total)
import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_08.txt", "r+").read().splitlines()

total_diff = 0

for line in input:
    extra = 2
    extra += line.count("\"")
    extra += line.count("\\")

    total_diff += extra

print(total_diff)

# input = open("inputs/2015_08.txt", "r+").read().splitlines()
#
# len_total = 0
# len_str = 0
#
# for line in input:
#     len_total += len(line)
#
#     print(line)
#     print(len(line))
#
#     line = line[1:-1]
#     line = line.replace("\\\\", "@")
#     line = line.replace("\\\"", "\"")
#     line = re.sub("\\\\x[0-9, a-f]{2}", "~", line)
#     len_str += len(line)
#
#     print(line)
#     print(len(line))
#
#
# print(len_total - len_str)
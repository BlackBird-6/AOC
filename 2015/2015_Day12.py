import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_12.txt", "r+").read()
total = 0

a = re.findall("[-1234567890]+", input)

for b in a:
    total += int(b)

print(total)

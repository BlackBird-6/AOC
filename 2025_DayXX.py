import random
import math
from itertools import *
from collections import *

import time
start_time = time.time()

f = open("inputs/2025_XX.txt", "r+").read().splitlines()

total = 0

for l in f:
    print(l)

print(f"Time elapsed: {time.time() - start_time}s")
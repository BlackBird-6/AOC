import random
import typing
import re
from itertools import *
from collections import *

import hashlib

input = "ckczppom"

count = 0
while True:
    encrypt = input + str(count)
    result = hashlib.md5(encrypt.encode()).hexdigest()
    if result.startswith("00000"):
        print(result)
        print(count)
        break
    count += 1

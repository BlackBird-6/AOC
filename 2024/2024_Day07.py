import random
import math
import itertools
import collections
import time
start_time = time.time()

input = open("inputs/2024_07.txt", "r+").read().splitlines()

total = 0

for l in input:
    l = l.split()

    target = int(l[0][:-1])
    nums = l[1:]
    print(l)

    found = False
    # (left, nums[0], nums[1]...)
    def dfs(current, nums):
        global total
        global found

        # Base case
        if current > target:
            return

        if len(nums) == 0:
            if current == target and not found:
                print("SUCCESS")
                found = True
                total += current
            return

        # Multiply
        dfs(current*int(nums[0]), nums[1:])

        # Add
        dfs(current+int(nums[0]), nums[1:])

        # PART 2 ADDON (6.427s)
        # # # # # # # #
        # Concatenate
        dfs(int(str(current) + str(nums[0])), nums[1:])
        # # # # # # # #
    dfs(0, nums)

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
# 0.124s

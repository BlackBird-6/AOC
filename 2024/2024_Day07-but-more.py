import random
import math
import itertools
import collections
import time
start_time = time.time()

input = open("inputs/2024_07.txt", "r+").read().splitlines()

total = 0

for i, l in enumerate(input):
    l = l.split()

    target = int(l[0][:-1])
    nums = l[1:] + l[1:]
    print(f"{i}/{len(input)}: {target} {nums}")

    symbols = []
    found = False
    # (left, nums[0], nums[1]...)
    def dfs(current, nums, eq):
        global total
        global found
        global symbols

        # Base case
        if current > target:
            return

        if len(nums) == 0:
            if current == target and not found:
                print("SUCCESS")
                symbols = eq

                found = True
                total += current
            return

        # Multiply
        dfs(current*int(nums[0]), nums[1:], eq + ["*"])

        # Add
        dfs(current+int(nums[0]), nums[1:], eq + ["+"])

        # PART 2 ADDON (2.044s)
        # Doubled input:
        # # # # # # # #
        # Concatenate
        dfs(int(str(current) + str(nums[0])), nums[1:], eq + ["|"])
        # # # # # # # #
    dfs(int(nums[0]), nums[1:], [])

    if found:
        equation = []
        for i in range(len(nums)):
            equation.append(nums[i])
            if i+1 != len(nums):
                equation.append(symbols[i])
        print("".join(equation))

print(total)

print(f"Time elapsed: {time.time() - start_time}s")
# 0.084s
# Doubled input: 54.398s, 8 successes (from 419)

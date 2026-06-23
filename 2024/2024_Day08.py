import itertools
import random
import math
from itertools import *
from collections import *

import time

start_time = time.time()

input = open("inputs/2024_08.txt", "r+").read().splitlines()

total = 0

grid = [[c for c in r] for r in input]

NUM_ROWS = len(grid)
NUM_COLUMNS = len(grid[0])

antennas = defaultdict(list)

for r in range(NUM_ROWS):
    for c in range(NUM_COLUMNS):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append((r, c))

antinodes = set()

for positions in antennas.values():
    print(positions)
    pairs = combinations(positions, 2)

    for p1, p2 in pairs:
        x1, y1 = p1
        x2, y2 = p2

        dx = x2 - x1
        dy = y2 - y1

        for i in range(50):
            ax = x2 + dx*i
            ay = y2 + dy*i

            if ax >= 0 and ax < NUM_ROWS and ay >= 0 and ay < NUM_COLUMNS:
                antinodes.add((ax, ay))

        for i in range(50):
            ax = x1 - dx*i
            ay = y1 - dy*i

            if ax >= 0 and ax < NUM_ROWS and ay >= 0 and ay < NUM_COLUMNS:
                antinodes.add((ax, ay))

for ax, ay in antinodes:
    grid[ax][ay] = "#"

for l in grid:
    print("".join(l))

print(antennas)
print(antinodes)
print(len(antinodes))

print(f"Time elapsed: {time.time() - start_time}s")

# import itertools
# import random
# import math
# from itertools import *
# from collections import *
#
# import time
# start_time = time.time()
#
# input = open("inputs/2024_08.txt", "r+").read().splitlines()
#
# total = 0
#
# grid = [[c for c in r] for r in input]
#
# NUM_ROWS = len(grid)
# NUM_COLUMNS = len(grid[0])
#
# antennas = defaultdict(list)
#
# for r in range(NUM_ROWS):
#     for c in range(NUM_COLUMNS):
#         if grid[r][c] != ".":
#             antennas[grid[r][c]].append((r, c))
#
# antinodes = set()
#
# for positions in antennas.values():
#     print(positions)
#     pairs = combinations(positions, 2)
#
#     for p1, p2 in pairs:
#         x1, y1 = p1
#         x2, y2 = p2
#
#         dx = x2 - x1
#         dy = y2 - y1
#
#         ax = x2 + dx
#         ay = y2 + dy
#
#         if ax >= 0 and ax < NUM_ROWS and ay >= 0 and ay < NUM_COLUMNS:
#             antinodes.add((ax, ay))
#
#         ax = x1 - dx
#         ay = y1 - dy
#
#         if ax >= 0 and ax < NUM_ROWS and ay >= 0 and ay < NUM_COLUMNS:
#             antinodes.add((ax, ay))
#
#
# for ax, ay in antinodes:
#     grid[ax][ay] = "#"
#
# for l in grid:
#     print("".join(l))
#
#
# print(antennas)
# print(antinodes)
# print(len(antinodes))
#
# print(f"Time elapsed: {time.time() - start_time}s")
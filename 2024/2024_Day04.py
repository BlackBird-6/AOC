import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2024_04.txt", "r+").read().splitlines()

print(input)
total = 0

grid = [[c for c in row] for row in input]

for r in grid:
    print("".join(r))

directions = [[1, 1],
              [1, -1],
              [-1, 1],
              [-1, -1]]

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "A":
            print((r, c))

            neighbors = []
            for dx, dy in directions:
                if r+dx >= 0 and c+dy >= 0:
                    try:
                        neighbors.append(grid[r+dx][c+dy])
                    except Exception as e:
                        continue

            if len(neighbors) < 4:
                continue

            if "X" in neighbors or "A" in neighbors:
                continue
            # 32
            # 10
            if neighbors[0] != neighbors[3] and neighbors[1] != neighbors[2]:
                total += 1

            print(neighbors)
            print(total)

print(total)


# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_04.txt", "r+").read().splitlines()
#
# print(input)
# total = 0
#
# grid = [[c for c in row] for row in input]
#
# for r in grid:
#     print("".join(r))
#
# directions = [[1, 1],
#               [1, 0],
#               [1, -1],
#               [0, 1],
#               [0, -1],
#               [-1, 1],
#               [-1, 0],
#               [-1, -1]]
#
# for r in range(len(grid)):
#     for c in range(len(grid[r])):
#         if grid[r][c] == "X":
#             print((r, c))
#             for dx, dy in directions:
#                 if r+3*dx >= 0 and c+3*dy >= 0:
#                     try:
#                         if grid[r+dx][c+dy] == "M" and grid[r+2*dx][c+2*dy] == "A" and grid[r+3*dx][c+3*dy] == "S":
#                             total += 1
#                     except Exception as e:
#                         continue
#
# print(total)
#

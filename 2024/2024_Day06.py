import random
import math
import itertools
import collections
import time
start_time = time.time()

input = open("inputs/2024_06.txt", "r+").read().splitlines()

total = 0

grid = [[c for c in r] for r in input]
print(grid)
#
#       (-1, 0)
# (0, -1)   0   (0, 1)
#       (1, 0)

NUM_ROWS = len(grid)
NUM_COLUMNS = len(grid[0])

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


obstacles = set()
res = []
initial_gr, initial_gc = 0, 0
for row in range(NUM_ROWS):
    for column in range(NUM_COLUMNS):
        if grid[row][column] == "#":
            obstacles.add((row, column))
        if grid[row][column] == "^":
            initial_gr, initial_gc = row, column


# Initial run to find all possible candidate cells to test
visited = set()
gr = initial_gr
gc = initial_gc
travel_dir = 0

while 0 <= gr and gr < NUM_ROWS and 0 <= gc and gc < NUM_COLUMNS:
    visited.add((gr, gc))
    dr, dc = directions[travel_dir]

    if (gr+dr, gc+dc) in obstacles:
        travel_dir += 1
        travel_dir = travel_dir % 4
        continue

    gr += dr
    gc += dc

visited = list(visited)
#
# for vr, vc in visited:
#     print(vr, vc)
#     try:
#         grid[vr][vc] = "o"
#     except Exception as e:
#         continue

for i, tuple in enumerate(visited):
    R, C = tuple
    if (R, C) in obstacles:
        continue
    else:
        print(f"{i}/{len(visited)} {(R, C)}")
        obstacles.add((R, C))

        infinite_loop = 0
        gr = initial_gr
        gc = initial_gc
        travel_dir = 0
        seen_states = set()
        move_count = 0

        while 0 <= gr and gr < NUM_ROWS and 0 <= gc and gc < NUM_COLUMNS:

            move_count += 1

            state = (gr, gc, travel_dir)

            if state in seen_states:
                res.append((R, C))
                break
            else:
                seen_states.add(state)

            dr, dc = directions[travel_dir]

            if (gr + dr, gc + dc) in obstacles:
                travel_dir += 1
                travel_dir = travel_dir % 4
                continue

            gr += dr
            gc += dc

        print(move_count, total)
        total += move_count
        obstacles.remove((R, C))

# for R in range(NUM_ROWS):
#     for C in range(NUM_COLUMNS):
#         if (R, C) in obstacles:
#             continue
#         else:
#             print((R, C))
#             obstacles.append((R, C))
#
#             infinite_loop = 0
#             gr = initial_gr
#             gc = initial_gc
#             travel_dir = 0
#
#             while 0 <= gr and gr < NUM_ROWS and 0 <= gc and gc < NUM_COLUMNS:
#                 dr, dc = directions[travel_dir]
#
#                 if (gr + dr, gc + dc) in obstacles:
#                     travel_dir += 1
#                     travel_dir = travel_dir % 4
#                     continue
#
#                 gr += dr
#                 gc += dc
#
#                 infinite_loop += 1
#                 if infinite_loop > 15000:
#                     res.append((R, C))
#
#                     break
#
#
#             obstacles.remove((R, C))




print(obstacles)

print(res)
print(len(res))

print(f"Time elapsed: {time.time() - start_time}s")
# 5.72 w/o prints
# 6.22 with prints

# import random
# import math
# import itertools
# import collections
#
# input = open("inputs/2024_06.txt", "r+").read().splitlines()
#
# total = 0
#
# grid = [[c for c in r] for r in input]
# print(grid)
# #
# #       (-1, 0)
# #(0, -1)   0   (0, 1)
# #       (1, 0)
#
# NUM_ROWS = len(grid)
# NUM_COLUMNS = len(grid[0])
#
# directions = [[-1, 0], [0, 1], [1,0], [0,-1]]
# travel_dir = 0
#
# obstacles = []
# visited = set()
# gr, gc = 0, 0
# for row in range(NUM_ROWS):
#     for column in range(NUM_COLUMNS):
#         if grid[row][column] == "#":
#             obstacles.append((row, column))
#         if grid[row][column] == "^":
#             gr, gc = row, column
#
# while 0 <= gr and gr < NUM_ROWS and 0 <= gc and gc < NUM_COLUMNS:
#     visited.add((gr, gc))
#     dr, dc = directions[travel_dir]
#
#     if (gr+dr, gc+dc) in obstacles:
#         travel_dir += 1
#         travel_dir = travel_dir % 4
#         continue
#
#     gr += dr
#     gc += dc
#
#
# visited = list(visited)
#
# for vr, vc in visited:
#     print(vr, vc)
#     try:
#         grid[vr][vc] = "o"
#     except Exception as e:
#         continue
#
# print(grid)
#
# for l in grid:
#     print("".join(l))
# print(len(visited))
import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_03.txt", "r+")

not_symbols = "1234567890."
numerals = "1234567890"
total = 0

chosen = []
checkpos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
scheckpos = [-2, -1, 0, 1, 2]

grid = ""
for line in input:
    grid += line
# print(grid)
grid = grid.split("\n")

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] not in not_symbols:
            for c in checkpos:
                if grid[i+c[0]][j+c[1]] in numerals and [i+c[0],j+c[1]] not in chosen:

                    selection = ""
                    num = ""
                    c_index = [-2, -1, 0, 1, 2]

                    for s in scheckpos:
                        selection += grid[i+c[0]][j+c[1]+s]

                    selection = re.sub("[.!@#$%^&*()/=-]", ".", selection)

                    for k, char in enumerate(selection):
                        if char not in numerals:
                            c_index[k] = 0
                    if selection[1] == ".":
                        c_index[0] = 0

                    if selection[3] == ".":
                        c_index[4] = 0
                    for ci in c_index:
                        chosen.append([i + c[0], j + c[1] + ci])

                    for k, char in enumerate(selection):
                        if char in numerals:
                            if k == 1 or k == 2 or k == 3:
                                num += char
                            if k == 0 and c_index[0] == -2:
                                num += char
                            if k == 4 and c_index[4] == 2:
                                num += char

                    print(selection)
                    print(c_index)
                    print(num)
                    total += int(num)

print(total)


                    #
                    #     chosen.append([i+c[0],j+c[1]+s])
                    #     # print("Chosen", chosen)
                    #
                    #     selection += grid[i+c[0]][j+c[1]+s]
                    # selection = re.split("[.!@#$%^&*()/=-]", selection)
                    # print(selection)
                    #
                    # for k, e in enumerate(selection):
                    #
                    #     if len(e) == 1:
                    #         print("## e = 1 ##")
                    #         print("####### k =", k)
                    #         if k == 0:
                    #             chosen.remove([i + c[0], j + c[1] - 2])
                    #         if k == 1:
                    #             chosen.remove([i + c[0], j + c[1] + 2])
                    #     if len(e) >= 2:
                    #         print(e)
                    #         total += int(e)




# for i, line in enumerate(input):
#     for j, char in enumerate(line):
#         if char != "\n":
#             grid[i][j] = char
#
#
# for i in range (140):
#     str = ""
#     for j in range(140):
#         str += grid[i][j]
#     print(str)
# filler = [[0 for i in range(140)] for i in range(140)]
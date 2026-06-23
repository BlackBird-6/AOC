import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2023_01.txt", "r+")

# numbers = "1234567890"
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
wordset = list(enumerate(words))

total = 0
for a in input:
    line = a.replace("\n","")
    first = -100
    last = -100
    checkstring = ""

    for i, char in enumerate(line):
        checkstring += char
        for word in words:
            if word in checkstring:
                if first == -100:
                    first = word
            if checkstring.endswith(word):
                last = word

    for num, word in list(enumerate(words)):
        if first == word and num < 10:
            first = num
        if last == word and num < 10:
            last = num


    total += 10*int(first) + int(last)

print(total)

    # if first in words:


        # if words in checkstring:
        #     print(char)

    # for word in words:
    #     if word in line:
    #         print(word)

    # for char in line:
    #     if char in numbers:
    #         if first == -100:
    #             first = int(char)
    #         last = int(char)
    #
    # total += 10*first + last
    # print(total)



#     Part 1
#     total = 0
# for a in input:
#     line = a.replace("\n","")
#     first = -100
#     last = -100
#     for char in line:
#         if char in numbers:
#             if first == -100:
#                 first = int(char)
#             last = int(char)
#
#     total += 10*first + last
#     print(total)

import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_07.txt", "r+").read().splitlines()
total = 0

wires = {}

def direct(a, b):
    try:
        wires[b] = wires[a]
    except: {}

def bitwise_and(a, b, d):

    # print(a, b, d)

    try:
        n1 = wires[a]
        n2 = wires[b]
        n3 = ""

        for i in range(16):
            if n1[i] == "1" and n2[i] == "1":
                n3 += "1"
            else:
                n3 += "0"

        wires[d] = n3
        print(n1, n2, n3)
    except: {}

def bitwise_or(a, b, d):

    # print(a, b, d)

    try:
        n1 = wires[a]
        n2 = wires[b]
        n3 = ""

        for i in range(16):
            if n1[i] == "1" or n2[i] == "1":
                n3 += "1"
            else:
                n3 += "0"

        wires[d] = n3
        print(n1, n2, n3)
    except: {}

def bitwise_not(a, d):

    # print(a, d)

    try:
        n1 = wires[a]
        n3 = ""

        for i in range(16):
            if n1[i] == "1":
                n3 += "0"
            else:
                n3 += "1"

        wires[d] = n3
        print(n1, n3)
    except: {}

def lshift(a, n, d):

    # print(a, n, d)
    n = int(n)

    try:
        n1 = wires[a]
        n3 = ""

        for i in range(n, 16):
            n3 += n1[i]
        for i in range (n):
            n3 += "0"

        wires[d] = n3
        print(n1, n3)
    except: {}

def rshift(a, n, d):

    # print(a, n, d)
    n = int(n)

    try:
        n1 = wires[a]
        n3 = ""

        for i in range (n):
            n3 += "0"

        for i in range(0, 16-n):
            n3 += n1[i]


        wires[d] = n3
        print(n1, n3)
    except: {}

def interpret(line):
    global wires
    mode = 0
    s_line = line.split()

    # Direct signal
    if len(s_line) == 3:
        direct(s_line[0], s_line[2])

    # Bitwise AND
    if "AND" in line:
        bitwise_and(s_line[0], s_line[2], s_line[4])

    # Bitwise OR
    if "OR" in line:
        bitwise_or(s_line[0], s_line[2], s_line[4])

    # NOT
    if "NOT" in line:
        bitwise_not(s_line[1], s_line[3])

    # LSHIFT
    if "LSHIFT" in line:
        lshift(s_line[0], s_line[2], s_line[4])

    # RSHIFT
    if "RSHIFT" in line:
        rshift(s_line[0], s_line[2], s_line[4])

# 0000110001101000
wires['b'] = "1010110110001110"
wires['c'] = "0000000000000000"
wires['1'] = "0000000000000001"

# interpret("b RSHIFT 2 -> e")

for i in range(120):
    for line in input:
        interpret(line)
        print(line)



print(wires)
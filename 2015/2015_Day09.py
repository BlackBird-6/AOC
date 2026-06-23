import random
import typing
import re
from itertools import *
from collections import *

input = open("inputs/2015_09.txt", "r+").read().splitlines()

graph = {}

for l in input:
    l = l.split()

    graph[l[0]] = {}
    graph[l[2]] = {}
#
# for l in input:
#     l = l.split()
#     graph[l[0]]

for g in graph.items():
    for node in graph:
        print(graph[node])

print(graph)
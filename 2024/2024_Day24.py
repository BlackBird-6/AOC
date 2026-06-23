import random
import typing
import re
from itertools import *
from collections import *


input = open("inputs/2024_24.txt", "r+").read().splitlines()

total = 0

gates = {}

instructions = []

for l in input:
    if ":" in l:
        gate, status = l.split(": ")
        gates[gate] = int(status)
    elif l == "":
        continue
    else:
        print(l)
        l = l.split()
        instructions.append((l[0], l[1], l[2], l[4]))


# So every layer has:
# x(N) XOR y(N) = PRECARRY(N)
# x(N) AND y(N) = CARRY(N+1)
# PRECARRY(N) XOR INTERLUDE(N) = Z(N)
# PRECARRY(N) AND INTERLUDE(N) = PRESUM(N)
# PRESUM(N) OR CARRY(N) = INTERLUDE(N+1)

precarry = {}
carry = {}
sum = []
presum = []
interlude = []
presum_links = {}
interlude_links = {2:"mrk"}
z = {}
for l in instructions:
    if l[0][1] in "0123456789":
        if l[1] == "XOR":
            precarry[int(l[0][1:])] = l[3]
        if l[1] == "AND":
            carry[int(l[0][1:])+1] = l[3]
    else:
        if l[1] == "XOR":
            z[l[3]] = [l[0], l[2]]
        if l[1] == "AND":
            presum.append([l[0], l[2], l[3]])
        if l[1] == "OR":
            interlude.append([l[0], l[2], l[3]])

print(precarry)
print(carry)
print(z)
print(sorted(z.keys()))
print(presum)
print(interlude)

errors = ['gvm', 'qsb', 'wmp', 'z17', 'z26', 'z39', 'qjj', 'gjc']
print(",".join(sorted(errors)))

# gvm', 'qsb', wmp
#
# # qsb, wmp, gvm, z17, z26, z39
## QJJ, GJC

# print(carry)
# print(interlude)
#
# for i in range(2, 45):
#     for set in presum:
#         if precarry[i] in set[:2] and interlude_links[i] in set[:2]:
#             presum_links[i] = set[2]
#             print(precarry[i], interlude[i], i)
#     for set in interlude:
#         print(presum_links[i], carry[i+1], set[:2])
#         if presum_links[i] in set[:2] and carry[i+1] in set[:2]:
#             interlude_links[i+1] = set[2]
#             print(interlude_links)
#             print(presum[i], carry[i], i)
#     # if precarry[i] in z[i] and carry[i] in z[i]:
#     #     print(i, z[i])
#     #     # sum.append([l[0], l[1], l[2], l[3]])
#     # print(l)
#


# 3210
#        # x00 XOR y00 = z00.         x00 AND y00 = CARRY(1) <wbd>
#      #  x00 XOR y00 = PRECARRY(0) <bfd>    x00 AND y00 = CARRY(1) <sfw>    PRECARRY(0) = z00
#                     PRECARRY(0) AND 0 = PRESUM(0) <hwt>    0 = 0 qkc
#   1
#  111 #  x01 XOR y01 = PRECARRY(1) <hfr>    x01 AND y01 = CARRY(2) <ktq>    PRECARRY(1) XOR CARRY(1) = z01
#  111                PRECARRY(1) AND CARRY(1) = PRESUM(1) <fhk>    PRESUM(1) OR CARRY(2) = INTERLUDE(2) <mrk>

#      # x02 XOR y02 = PRECARRY(2) <bfd>    x02 AND y02 = CARRY(3) <sfw>    PRECARRY(2) XOR INTERLUDE(2) = z02
#                     PRECARRY(2) AND INTERLUDE(2) = PRESUM(2) <hwt>    PRESUM(2) OR CARRY(3) = INTERLUDE(3) <qkc>

#      # x03 XOR y03 = PRECARRY(3) <nmb>    x03 AND y03 = CARRY(3) <wqk>    PRECARRY(3) XOR INTERLUDE(3) = z03
#                       PRECARRY(3) AND INTERLUDE(3) = PRESUM(3) <gdm>  PRESUM(3) OR CARRY(4) = INTERLUDE(4) <www>
#
#       PRESUM_LINKS 11 was not generated.
# x10 xor y10 --> fvg (PRECARRY(10))    CARRY(10) <fsw>
# PRECARRY(10) AND INTERLUDE(10) trw  --> bng PRESUM(10)    PRESUM(10) bng or fsw = interlude(11) JDM

#  x11 XOR y11 = PRECARRY(11) <gjc?>    x11 AND y11 = CARRY(11) <qjj?>  PRECARRY(11) <QJJ!!> XOR <JDM> = <z11>
#  PRECARRY(11) <QJJ!> AND INTERLUDE(11) JDM -> ckv PRESUM(11)         gjc or ckv --> sfm <INTERLUDE(12)>   PRESUM(
# so QJJ and GJC was swapped.
# PRECARRY(3) qjj AND INTERLUDE(11) jdm -->


# 0000 <...>

# So every layer has:
# x(N) XOR y(N) = PRECARRY(N)
# x(N) AND y(N) = CARRY(N+1)
# PRECARRY(N) XOR INTERLUDE(N) = Z(N)
# PRECARRY(N) AND INTERLUDE(N) = PRESUM(N)
# PRESUM(N) OR CARRY(N) = INTERLUDE(N+1)

# <(x01 XOR y01) AND CARRY(1)> OR (z00 AND y00) = INTERLUDE(N+1) <carry as a determination of 3>
# So we need to identify triples that fail this property.


#
# print(final)
# print(num)
# gate1, method, gate2, gate3

# import random
# import typing
# import re
# from itertools import *
# from collections import *
#
# input = open("inputs/2024_24.txt", "r+").read().splitlines()
#
# total = 0
#
# gates = {}
#
# instructions = []
#
# for l in input:
#     if ":" in l:
#         gate, status = l.split(": ")
#         gates[gate] = int(status)
#     elif l == "":
#         continue
#     else:
#         l = l.split()
#         instructions.append((l[0], l[1], l[2], l[4]))
#
# for i in range(1000):
#     for gate1, method, gate2, gate3 in instructions:
#         if gate1 in gates.keys():
#             if gate2 in gates.keys():
#                 A = gates[gate1]
#                 B = gates[gate2]
#
#                 if method == "AND":
#                     gates[gate3] = int(A and B)
#
#                 if method == "OR":
#                     gates[gate3] = int(A or B)
#
#                 if method == "XOR":
#                     gates[gate3] = int(A != B)
#
# final = []
# for gate, val in gates.items():
#     if gate.startswith("z"):
#         final.append((gate, val))
#
# final = sorted(final, key=lambda val: val[0], reverse=True)
#
# num = int("".join(str(val[1]) for val in final), 2)
# print(num)
#
# # print(final)
#
# for l in input:
#     print(l)
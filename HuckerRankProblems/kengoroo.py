# There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward ).
# Each kangaroo takes the same amount of time to make a jump, regardless of distance. That is, if kangaroo one jumps
#  3 meters and kangaroo two jumps 5 meters, they each do it in one second, for example.
#
# Given the starting locations and jump distances for each kangaroo, determine if and when they will land at the same
# location at the same time.
#
# Input Format
#
# A single line of four space-separated integers denoting the respective values of , , , and .

import sys

def kangaroo(x1, v1, x2, v2):

    if v2 >= v1:
        return 'NO'


    newX1 = x1
    newX2 = x2
    delta = x2 - x1

    while delta > 0:
        newX1 = newX1 + v1
        newX2 = newX2 + v2
        delta = newX2 - newX1

    if delta == 0:
        return'YES'

    return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

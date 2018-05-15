

import sys

# Context
# Given a  2D Array, :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
#
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.
#
# Input Format
#
# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .
#
# Constraints
#
# Output Format
#
# Print the largest (maximum) hourglass sum found in .
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
#Ex2:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Ex1:
# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5

# Ex2:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#
# Ans=19

N = 6
hourglassDiam = 3
arr = []
hourglassMax = -100000
for arr_i in range(N):
    arr_t = [int(arr_temp) for arr_temp in raw_input().strip().split(' ')]
    arr.append(arr_t)

for row in range(0, N - hourglassDiam + 1):
    for col in range(0, N - hourglassDiam + 1):
        maxNum = arr[row][col] + arr[row][col + 1] + arr[row][col + 2]
        maxNum += arr[row + 1][col + 1]
        maxNum += arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
        if (maxNum > hourglassMax):
            hourglassMax = maxNum

print(hourglassMax)


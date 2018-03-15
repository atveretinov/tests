# Lily has a chocolate bar consisting of a row of n squares where each square has an integer written on it.
# She wants to share it with Ron for his birthday, which falls on month m and day d. Lily wants to give Ron a piece of
# chocolate only if it contains m consecutive squares whose integers sum to d.
# Given m,d , and the sequence of integers written on each square of Lily's chocolate bar, how many different ways can' \
# 'Lily break off a piece of chocolate to give to Ron?

import sys

def solve(n, s, d, m):
    result = 0
    #compare len of array and "month"
    if m > n:
        return 0

    #compare "day" and summ of ol array elements
    if d > sum(s):
        return 0
    #create a cycle for comparing sum of "month" elements and  value of "day"
    for i in range(0,len(s)-m+1):
        if sum(s[i:i+m]) == d:
            result = result + 1
    return result

if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    d, m = input().strip().split(' ')
    d, m = [int(d), int(m)]
    result = solve(n, s, d, m)
    print(result)


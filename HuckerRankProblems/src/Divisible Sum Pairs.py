# You are given an array of n integers a0,a1,...,an-1 , and a positive integer, k . Find and print the number of (i,j)
# pairs where i<j and ai +aj is divisible by k.


import sys

def divisibleSumPairs(n, k, ar):

    counter = 0

    for i in range(0,len(ar)+1):
        for j in range (i+1,len(ar)):
            if (ar[i] +ar[j])%k == 0:
                counter = counter + 1
    return counter


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
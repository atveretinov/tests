# Consider an array of  n integers, A = [a0,a1,...,an-1] . The distance between two indices,i and j, is denoted by
# di,j =|i-j| . Given A , find the minimum di,j such that ai=aj and i!=j . In other words, find the minimum distance
# between any pair of equal elements in the array. If no such value exists, print -1 .
# Note: denotes the absolute value of a.

import sys

def minimumDistances(a):
    distances = list()

    for i in range(0,len(a)+1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                distances.append(abs(i-j))


    if len(distances) == 0:
        return "-1"
    minDist = min(distances)
    return minDist





if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)

def countApplesAndOranges(s, t, a, b, apple, orange):
    larryScore = 0
    robScore = 0
    for i in range(0,len(apple)):
        if s <= a+apple[i] <= t:
            larryScore = larryScore + 1
    for i in range(0,len(orange)):
        if s <= b+orange[i] <= t:
            robScore = robScore + 1
    print(larryScore)
    print(robScore)


s = 7
t = 11
a = 5
b = 15
apple = [-2,2,1]
orange = [5,-6]
countApplesAndOranges(s, t, a, b, apple, orange)
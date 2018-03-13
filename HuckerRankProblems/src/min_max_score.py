# Maria plays games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game
# sequentially in an array defined as . After each game , she checks to see if score breaks her record for most or least
# points scored so far during that season.
# Given Maria's array of for a season of games, find and print the number of times she breaks her record for most and
# least points scored during the season.
# Note: Assume her records for most and least points at the start of the season are the number of points scored during
# the first game of the season.


#PLAN:
#create an max and min variables
#create the counter for min and max
#go through the array and found the number of changing of min and max
# TODO
import sys

def breakingRecords(score):

    maxscore = score[0]
    minscore = score[0]
    maxcount = 0
    mincount = 0

    for i in range(0,len(score)):
        if score[i] > maxscore:
            maxscore = score[i]
            maxcount = maxcount + 1
        if score[i] < minscore:
            minscore = score[i]
            mincount = mincount + 1

    return (maxcount,mincount)


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))



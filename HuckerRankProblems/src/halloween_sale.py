
# You wish to buy video games from the famous online video game store Mist.
#
# Usually, all games are sold at the same price,p dollars. However, they are planning to have the seasonal Halloween
# Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale
# will be sold at p dollars, but every subsequent game you buy will be sold at exactly d dollars less than the cost of the
# previous one you bought. This will continue until the cost becomes less than or equal to m dollars, after which every
# game you buy will cost m dollars each.

import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    i=0
    myMoney = s
    numberOfGames = 0
    while True:
        if myMoney < p-i*d:
            break

        if myMoney < m:
            break


        if p-i*d <= m:
            myMoney = myMoney - m
            numberOfGames = numberOfGames +1

        else:
            myMoney = myMoney - (p-i*d)
            numberOfGames = numberOfGames +1

        i = i+1
    return numberOfGames


if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
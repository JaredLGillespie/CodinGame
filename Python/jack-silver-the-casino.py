# https://www.codingame.com/training/easy/jack-silver-the-casino


import math


def solution():
    rounds = int(input())
    cash = int(input())
    for _ in range(rounds):
        play = input().split()
        bet = math.ceil(cash / 4)
        cash -= bet

        if play[1] == 'ODD':
            if int(play[0]) % 2 == 1:
                cash += bet * 2
        elif play[1] == 'EVEN':
            if int(play[0]) % 2 == 0 and int(play[0]) != 0:
                cash += bet * 2
        else:
            if int(play[0]) == int(play[2]):
                cash += 36 * bet

    print(cash)


solution()

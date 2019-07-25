# https://www.codingame.com/training/easy/addem-up

from heapq import *


def solution():
    num_cards = int(input())
    cards = list(map(int, input().split()))
    heapify(cards)

    cost = 0
    while len(cards) > 1:
        card1 = heappop(cards)
        card2 = heappop(cards)
        cost += card1 + card2
        heappush(cards, card1 + card2)

    print(cost)


solution()

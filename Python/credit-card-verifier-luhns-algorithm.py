# https://www.codingame.com/training/easy/credit-card-verifier-luhns-algorithm


def solution():
    for _ in range(int(input())):
        card = [int(x) for x in input() if x != ' ']
        doubling = sum(x * 2 - 9 if x * 2 > 9 else x * 2 for x in card[-2::-2])
        odds = sum(card[-1::-2])
        print('YES' if (doubling + odds) % 10 == 0 else 'NO')


solution()

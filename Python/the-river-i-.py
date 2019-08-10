# https://www.codingame.com/training/easy/the-river-i-


def solution():
    r1, r2 = int(input()), int(input())
    while r1 != r2:
        if r1 < r2:
            r1 += sum(map(int, str(r1)))
        else:
            r2 += sum(map(int, str(r2)))
    print(r1)


solution()

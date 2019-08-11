# https://www.codingame.com/training/easy/smooth


def solution():
    for _ in range(int(input())):
        f = int(input())
        while f > 1:
            if f % 5 == 0:
                f //= 5
            elif f % 3 == 0:
                f //= 3
            elif f % 2 == 0:
                f //= 2
            else:
                print('DEFEAT')
                break
        else:
            print('VICTORY')


solution()

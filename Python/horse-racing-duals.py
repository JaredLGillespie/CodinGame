# https://www.codingame.com/training/easy/horse-racing-duals


def solution():
    num_horses = int(input())
    horses = sorted([int(input()) for _ in range(num_horses)])

    d = float('inf')
    for i in range(1, num_horses):
        d = min(d, horses[i] - horses[i - 1])

    print(d)


solution()

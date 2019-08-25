# https://www.codingame.com/training/easy/horse-racing-hyperduals


def solution():
    num_horses = int(input())
    horses = [list(map(int, input().split())) for _ in range(num_horses)]
    closest = float('inf')

    for i in range(1, len(horses)):
        for j in range(i):
            closest = min(closest, abs(horses[j][0] - horses[i][0]) + abs(horses[j][1] - horses[i][1]))

    print(closest)


solution()

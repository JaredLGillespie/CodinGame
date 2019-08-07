# https://www.codingame.com/training/easy/count-as-i-count


def solution():
    initial_score = int(input())
    combs = [[1, 0, 0, 0, 0]] + [[0, 0, 0, 0, 0] for _ in range(50 - initial_score)]

    for i in range(1, len(combs)):
        for j in range(max(0, i - 12), i):
            for k in range(1, 5):
                combs[i][k] += combs[j][k - 1] * (2 - (j == i - 1))
    print(sum(combs[i][1:]))


solution()

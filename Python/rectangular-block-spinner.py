# https://www.codingame.com/training/easy/rectangular-block-spinner


def solution():
    size = int(input())
    angle = int(input())
    ascii = [input()[::2] for _ in range(size)]

    for _ in range(4 - ((angle % 360 // 90 + 1) % 4)):
        ascii = list(zip(*reversed(ascii)))

    for i in range(size):
        print('{0}{1}{0}'.format(
            ' ' * (size - i - 1),
            ' '.join([ascii[i - j][j] for j in range(i + 1)])
        ))

    for i in range(1, size):
        print('{0}{1}{0}'.format(
            ' ' * i,
            ' '.join([ascii[size - j - 1][i + j] for j in range(size - i)])
        ))


solution()

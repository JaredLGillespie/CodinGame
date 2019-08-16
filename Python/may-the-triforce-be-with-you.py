# https://www.codingame.com/training/easy/may-the-triforce-be-with-you


def draw_top(size):
    for i in range(1, size + 1):
        if i == 1:
            print('.' + ' ' * (size * 2 - i - 1), end='')
        else:
            print(' ' * (size * 2 - i), end='')
        print('*' * (i * 2 - 1))


def draw_bottom(size):
    for i in range(1, size + 1):
        print(' ' * (size - i), end='')
        print('*' * (i * 2 - 1), end='')
        print(' ' * ((size - i) * 2 + 1), end='')
        print('*' * (i * 2 - 1))


def solution():
    size = int(input())
    draw_top(size)
    draw_bottom(size)


solution()

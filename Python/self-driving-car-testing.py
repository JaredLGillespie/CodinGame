# https://www.codingame.com/training/easy/self-driving-car-testing


def get_next_pos(pos, commands):
    for command in commands:
        n, d = int(command[:-1]), command[-1]
        for _ in range(n):
            if d == 'L':
                pos -= 1
            elif d == 'R':
                pos += 1
            yield pos


def solution():
    n = int(input())
    pos, *commands = input().split(';')
    pos = int(pos)
    pos_iter = get_next_pos(pos, commands)

    for _ in range(n):
        rep, pattern = input().split(';')
        for _ in range(int(rep)):
            road = list(pattern)
            road[next(pos_iter) - 1] = '#'
            print(''.join(road))


solution()

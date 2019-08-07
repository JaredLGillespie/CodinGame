# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1


def solution():
    width, height = map(int, input().split())
    num_turns = int(input())
    x, y = map(int, input().split())
    l, r, u, d = 0, width - 1, 0, height - 1

    while True:
        bomb_dir = input()
        if bomb_dir[0] == 'D':
            u = y + 1
        elif bomb_dir[0] == 'U':
            d = y - 1
        if bomb_dir[-1] == 'L':
            r = x - 1
        elif bomb_dir[-1] == 'R':
            l = x + 1

        x = (l + r) // 2
        y = (u + d) // 2
        print('{} {}'.format(x, y))


solution()

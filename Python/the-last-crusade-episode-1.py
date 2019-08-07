# https://www.codingame.com/training/medium/the-last-crusade-episode-1


def solution():
    w, h = map(int, input().split())
    grid = [input().split() for _ in range(h)]
    ex = int(input())

    while True:
        xi, yi, pos = input().split()
        xi, yi = int(xi), int(yi)
        room = int(grid[yi][xi])
        if room == 0: print('{} {}'.format(xi, yi))
        elif room in (1, 3, 7, 8, 9): print('{} {}'.format(xi, yi + 1))
        elif room == 2:
            if pos == 'LEFT': print('{} {}'.format(xi + 1, yi))
            elif pos == 'RIGHT': print('{} {}'.format(xi - 1, yi))
            else: print('{} {}'.format(xi, yi))
        elif room == 4:
            if pos == 'TOP': print('{} {}'.format(xi - 1, yi))
            elif pos == 'RIGHT': print('{} {}'.format(xi, yi + 1))
            else: print('{} {}'.format(xi, yi))
        elif room == 5:
            if pos == 'TOP': print('{} {}'.format(xi + 1, yi))
            elif pos == 'LEFT': print('{} {}'.format(xi, yi + 1))
            else: print('{} {}'.format(xi, yi))
        elif room == 6:
            if pos == 'LEFT': print('{} {}'.format(xi + 1, yi))
            else: print('{} {}'.format(xi - 1, yi))
        elif room == 10: print('{} {}'.format(xi - 1, yi))
        elif room == 11: print('{} {}'.format(xi + 1, yi))
        else: print('{} {}'.format(xi, yi + 1))


solution()

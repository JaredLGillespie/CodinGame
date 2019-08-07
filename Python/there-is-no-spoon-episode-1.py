# https://www.codingame.com/training/medium/there-is-no-spoon-episode-1


def solution():
    width = int(input())
    height = int(input())
    grid = [input() for _ in range(height)]

    for x in range(width):
        for y in range(height):
            if grid[y][x] == '.': continue
            rx = ry = bx = by = -1

            for i in range(x + 1, width):
                if grid[y][i] == '.': continue
                rx, ry = i, y
                break

            for i in range(y + 1, height):
                if grid[i][x] == '.': continue
                bx, by = x, i
                break

            print('{} {} {} {} {} {}'.format(x, y, rx, ry, bx, by))


solution()

# https://www.codingame.com/training/easy/brick-in-the-wall


def solution():
    max_row_bricks = int(input())
    num_bricks = int(input())
    bricks = map(int, input().split())

    work = 0
    row, row_bricks = 1, 0
    for brick in sorted(bricks, reverse=True):
        work += ((row - 1) * 6.5 / 100) * 10 * brick
        row_bricks += 1
        if row_bricks == max_row_bricks:
            row_bricks = 0
            row += 1

    print('{0:.3f}'.format(work))


solution()

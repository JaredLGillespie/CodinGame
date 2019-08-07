# https://www.codingame.com/training/easy/detective-pikaptcha-ep1


def get_neighbors(row, col, grid):
    if row > 0: yield row - 1, col
    if row < len(grid) - 1: yield row + 1, col
    if col > 0: yield row, col - 1
    if col < len(grid[row]) - 1: yield row, col + 1


def solution():
    width, height = [int(i) for i in input().split()]
    grid = [list(input()) for _ in range(height)]

    for row in range(height):
        for col in range(width):
            if grid[row][col] == '#': continue
            grid[row][col] = str(sum(grid[r][c] != '#' for r, c in get_neighbors(row, col, grid)))

    for row in grid:
        print(''.join(row))


solution()

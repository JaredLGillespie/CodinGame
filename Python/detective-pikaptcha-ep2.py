# https://www.codingame.com/training/easy/detective-pikaptcha-ep2


def get_next_passage(row, col, directions, grid):
    direction_pos_offsets = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
    for direction in directions:
        dpo = direction_pos_offsets[direction]
        if is_passage(row + dpo[0], col + dpo[1], grid):
            return (row + dpo[0], col + dpo[1]), direction
    return (-1, -1), ''


def get_next_pos(row, col, direction, side, grid):
    if direction == '^':
        if side == 'L': return get_next_passage(row, col, '<^>v', grid)
        else: return get_next_passage(row, col, '>^<v', grid)
    elif direction == '>':
        if side == 'L': return get_next_passage(row, col, '^>v<', grid)
        else: return get_next_passage(row, col, 'v>^<', grid)
    elif direction == 'v':
        if side == 'L': return get_next_passage(row, col, '>v<^', grid)
        else: return get_next_passage(row, col, '<v>^', grid)
    else:
        if side == 'L': return get_next_passage(row, col, 'v<^>', grid)
        else: return get_next_passage(row, col, '^<v>', grid)


def is_passage(row, col, grid):
    if row < 0 or row > len(grid) - 1: return False
    if col < 0 or col > len(grid[row]) - 1: return False
    return grid[row][col] != '#'


def solution():
    width, height = map(int, input().split())
    grid = [list(input()) for _ in range(height)]
    side = input()

    opos = pos = [(r, c) for r in range(height) for c in range(width) if grid[r][c] in '>v<^'][0]
    direction = grid[pos[0]][pos[1]]
    grid[pos[0]][pos[1]] = 0
    left_original_pos = False

    while pos != opos or not left_original_pos:
        left_original_pos = True
        pos, direction = get_next_pos(pos[0], pos[1], direction, side, grid)
        if pos == (-1, -1): break
        grid[pos[0]][pos[1]] = int(grid[pos[0]][pos[1]]) + 1

    for row in grid:
        print(''.join(map(str, row)))


solution()

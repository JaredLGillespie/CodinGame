# https://www.codingame.com/training/easy/rooks-movements


BOARD_SIZE = 8
BOARD_TRANS = {-1: '-', 1: 'x'}


def pos_trans(a):
    return ord(a[0]) - ord('a'), int(a[1]) - 1


def pos_trans_rev(a):
    return chr(a[0] + ord('a')), str(a[1] + 1)


def check_horizontal(board, ipos, ix, y):
    moves = []
    for x in range(ix - 1, -1, -1):
        px, py = pos_trans_rev((x, y))
        m = board[y][x]
        if m == 0:
            break
        else:
            moves.append('R{}{}{}{}'.format(ipos, BOARD_TRANS[m], px, py))
        if m == 1: break

    for x in range(ix + 1, BOARD_SIZE):
        px, py = pos_trans_rev((x, y))
        m = board[y][x]
        if m == 0:
            break
        else:
            moves.append('R{}{}{}{}'.format(ipos, BOARD_TRANS[m], px, py))
        if m == 1: break

    return moves


def check_vertical(board, ipos, x, iy):
    moves = []
    for y in range(iy - 1, -1, -1):
        px, py = pos_trans_rev((x, y))
        m = board[y][x]
        if m == 0:
            break
        else:
            moves.append('R{}{}{}{}'.format(ipos, BOARD_TRANS[m], px, py))
        if m == 1: break

    for y in range(iy + 1, BOARD_SIZE):
        px, py = pos_trans_rev((x, y))
        m = board[y][x]
        if m == 0:
            break
        else:
            moves.append('R{}{}{}{}'.format(ipos, BOARD_TRANS[m], px, py))
        if m == 1: break

    return moves


def solution():
    ipos = input()
    ix, iy = pos_trans(ipos)
    num_pieces = int(input())

    board = [[-1] * BOARD_SIZE for _ in range(8)]
    for _ in range(num_pieces):
        color, position = input().split()
        px, py = pos_trans(position)
        board[py][px] = int(color)

    moves = []
    moves.extend(check_horizontal(board, ipos, ix, iy))
    moves.extend(check_vertical(board, ipos, ix, iy))

    for move in sorted(moves):
        print(move)


solution()

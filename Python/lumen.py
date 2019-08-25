# https://www.codingame.com/training/easy/lumen


def get_neighbors(col, row, room_size):
    if room_size == 1: return

    if row > 0:
        yield col, row - 1
        if col > 0: yield col - 1, row - 1
        if col < room_size - 1: yield col + 1, row - 1

    if row < room_size - 1:
        yield col, row + 1
        if col > 0: yield col - 1, row + 1
        if col < room_size - 1: yield col + 1, row + 1

    if col > 0: yield col - 1, row
    if col < room_size - 1: yield col + 1, row


def fill_light(col, row, light_level, room, room_size):
    if light_level == 0: return
    if room[col][row] in ('X', 'C'):
        room[col][row] = light_level
    elif room[col][row] >= light_level:
        return

    room[col][row] = light_level

    for nc, nr in get_neighbors(col, row, room_size):
        fill_light(nc, nr, light_level - 1, room, room_size)


def count_dark_spots(room, room_size):
    ret = 0
    for col in range(room_size):
        for row in range(room_size):
            if room[col][row] in ('X', 0):
                ret += 1
    return ret


def solution():
    room_size = int(input())
    base_light = int(input())
    candles = []

    room = []
    for col in range(room_size):
        room.append(input().split())
        for row, c in enumerate(room[-1]):
            if c == 'C':
                candles.append((col, row))

    for col, row in candles:
        fill_light(col, row, base_light, room, room_size)

    dark_spots = count_dark_spots(room, room_size)
    print(dark_spots)


solution()

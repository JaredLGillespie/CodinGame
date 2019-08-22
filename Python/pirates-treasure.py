# https://www.codingame.com/training/easy/pirates-treasure


def get_neighbors(x, y, width, height):
    if x > 0:
        yield x - 1, y
        if y > 0: yield x - 1, y - 1
        if y < height - 1: yield x - 1, y + 1

    if x < width - 1:
        yield x + 1, y
        if y > 0: yield x + 1, y - 1
        if y < height - 1: yield x + 1, y + 1

    if y > 0: yield x, y - 1
    if y < height - 1: yield x, y + 1


def count_land_neighbors(x, y, width, height, treasure_map):
    return sum(treasure_map[ny][nx] for nx, ny in get_neighbors(x, y, width, height))


def is_treasure(x, y, width, height, treasure_map):
    if treasure_map[y][x] == 1: return False
    land_neighbors = count_land_neighbors(x, y, width, height, treasure_map)

    if land_neighbors == 3:
        return (x, y) in [(0, 0), (0, height - 1), (width - 1, 0), (width - 1, height - 1)]
    elif land_neighbors == 5:
        return x in (0, width - 1) or y in (0, height - 1)
    elif land_neighbors == 8:
        return x not in (0, width - 1) and y not in (0, height - 1)

    return False


def solution():
    width = int(input())
    height = int(input())

    treasure_map = []
    for _ in range(height):
        treasure_map.append(list(map(int, input().split())))

    for y in range(height):
        for x in range(width):
            if is_treasure(x, y, width, height, treasure_map):
                print('{} {}'.format(x, y))


solution()

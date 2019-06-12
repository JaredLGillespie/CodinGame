# https://www.codingame.com/training/easy/dead-mens-shot


def within_polygon(x, y, points, num_corners):
    pos, neg = False, False

    for i in range(num_corners):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % num_corners]
        d = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        if d > 0:
            pos = True
        else:
            neg = True

        if pos == neg: return False
    return True


def solution():
    points = []

    num_corners = int(input())
    for _ in range(num_corners):
        points.append(list(map(int, input().split())))

    num_shots = int(input())
    for _ in range(num_shots):
        x, y = map(int, input().split())
        if within_polygon(x, y, points, num_corners):
            print('hit')
        else:
            print('miss')


solution()

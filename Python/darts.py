# https://www.codingame.com/training/easy/darts


def within_polygon(x, y, points):
    pos, neg = False, False

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        d = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)

        if d > 0:
            pos = True
        else:
            neg = True

        if pos == neg: return False
    return True


def within_square(x, y, size):
    l = size / 2 + 0.0001
    square_points = [(l, l), (l, -l), (-l, -l), (-l, l)]
    return within_polygon(x, y, square_points)


def within_diamond(x, y, size):
    l = size / 2 + 0.0001
    diamond_points = [(0, l), (l, 0), (0, -l), (-l, 0)]
    return within_polygon(x, y, diamond_points)


def within_circle(x, y, size):
    l = size / 2 + 0.0001
    return ((x ** 2) + (y ** 2)) ** 0.5 <= l


def solution():
    size = int(input())
    num_competitors = int(input())
    competitors = {}
    competitor_order = {}

    for i in range(num_competitors):
        name = input()
        competitors[name] = 0
        competitor_order[name] = i

    num_throws = int(input())

    for _ in range(num_throws):
        name, x, y = input().split()
        x = int(x)
        y = int(y)
        competitors[name] += 5 * (
                within_circle(x, y, size) +
                within_square(x, y, size) +
                within_diamond(x, y, size)
        )

    for name in sorted(competitors, key=lambda x: (-competitors[x], competitor_order[x])):
        print('{} {}'.format(name, competitors[name]))


solution()

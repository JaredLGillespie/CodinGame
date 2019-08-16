# https://www.codingame.com/training/easy/morellets-random-lines


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_point_on_line(x, y, line):
    return line[0] * x + line[1] * y + line[2] == 0


def reduce_equation(a, b, c):
    g = gcd(gcd(a, b), c)
    return a // g, b // g, c // g


def get_line(x1, y1, x2, y2):
    m = (y1 - y2) / (x1 - x2)
    b = (x1 * y2 - x2 * y1) / (x1 - x2)
    return m, b


def get_intersection_point_between_lines(sm, sb, la, lb, lc):
    x = (-lb * sb - lc) / (la + lb * sm)
    y = sm * x + sb
    return x, y


def does_segment_intersect_line(sm, sb, la, lb, lc, xa, ya, xb, yb):
    px, py = get_intersection_point_between_lines(sm, sb, la, lb, lc)
    return min(xa, xb) <= px <= max(xa, xb) and min(ya, yb) <= py <= max(ya, yb)


def solution():
    xa, ya, xb, yb = map(int, input().split())
    num_lines = int(input())
    equations = {reduce_equation(*map(int, input().split()))
                 for _ in range(num_lines)}

    for x, y in ((xa, ya), (xb, yb)):
        if any(is_point_on_line(x, y, line) for line in equations):
            print('ON A LINE')
            return

    sm, sb = get_line(xa, ya, xb, yb)
    num_crossed_lines = sum(
        does_segment_intersect_line(sm, sb, a, b, c, xa, ya, xb, yb)
        for a, b, c in equations
    )

    print('YES' if num_crossed_lines % 2 == 0 else 'NO')


solution()


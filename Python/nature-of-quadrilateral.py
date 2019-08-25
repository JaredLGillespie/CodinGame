# https://www.codingame.com/training/easy/nature-of-quadrilaterals


import math


def get_length(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def get_angle(x1, y1, x2, y2, x3, y3):
    ang = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    return ang + 360 if ang < 0 else ang


def print_answer(a, b, c, d, shape):
    print('{}{}{}{} is a {}.'.format(a, b, c, d, shape))


def get_lengths(ax, ay, bx, by, cx, cy, dx, dy):
    return [get_length(ax, ay, bx, by),
            get_length(bx, by, cx, cy),
            get_length(cx, cy, dx, dy),
            get_length(dx, dy, ax, ay)]


def get_angles(ax, ay, bx, by, cx, cy, dx, dy):
    return [get_angle(ax, ay, bx, by, cx, cy),
            get_angle(bx, by, cx, cy, dx, dy),
            get_angle(cx, cy, dx, dy, ax, ay),
            get_angle(dx, dy, ax, ay, bx, by)]


def solution():
    num_quads = int(input())
    for _ in range(num_quads):
        text = input().split()
        a, b, c, d = text[0], text[3], text[6], text[9]
        ax, ay = map(int, text[1:3])
        bx, by = map(int, text[4:6])
        cx, cy = map(int, text[7:9])
        dx, dy = map(int, text[10:12])

        lengths = get_lengths(ax, ay, bx, by, cx, cy, dx, dy)
        angles = get_angles(ax, ay, bx, by, cx, cy, dx, dy)

        if len(set(angles)) == 1:
            if len(set(lengths)) == 1:
                print_answer(a, b, c, d, 'square')
            else:
                print_answer(a, b, c, d, 'rectangle')
        elif len(set(lengths)) == 1:
            print_answer(a, b, c, d, 'rhombus')
        elif lengths[0] == lengths[2] and lengths[1] == lengths[3]:
            print_answer(a, b, c, d, 'parallelogram')
        else:
            print_answer(a, b, c, d, 'quadrilateral')


solution()

# https://www.codingame.com/training/easy/the-travelling-salesman-problem


def dist_between(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def find_closest(cur_point, points, used_points):
    closest_dist = float('inf')
    closest_point_index = -1
    for i, point in enumerate(points):
        if used_points[i]: continue
        dist = dist_between(cur_point, point)
        if dist < closest_dist:
            closest_dist = dist
            closest_point_index = i

    used_points[closest_point_index] = True
    return points[closest_point_index], closest_dist


def solution():
    num_points = int(input())
    points = []
    used_points = [False] * num_points
    first_point = None

    for i in range(num_points):
        x, y = map(int, input().split())
        if i == 0:
            first_point = (x, y)
        else:
            points.append((x, y))

    cur_point = first_point
    total_dist = 0
    for _ in range(num_points - 1):
        cur_point, dist = find_closest(cur_point, points, used_points)
        total_dist += dist

    total_dist += dist_between(cur_point, first_point)
    print(round(total_dist))


solution()

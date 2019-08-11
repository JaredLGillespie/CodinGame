# https://www.codingame.com/training/easy/the-frog-jump-1


import math


def solution():
    frog_number = int(input())
    distances = list(map(float, input().split()))

    x, y = map(int, input().split())
    mass = int(input())
    alpha = math.radians(int(input()))
    speed = float(input())
    a, b = map(float, input().split())

    speed_x = math.cos(alpha) * speed
    speed_y = math.sin(alpha) * speed

    delta = speed_y ** 2 - 4 * (b / 2) * y
    time = (-speed_y - delta ** 0.5) / b
    dist = (a / 2 * time ** 2) + (speed_x * time) + x
    dist = round(dist, 2)

    distances.append(dist)
    distances = sorted(distances, reverse=True)

    for i, distance in enumerate(distances):
        if distance == dist:
            break

    print(i + 1)


solution()

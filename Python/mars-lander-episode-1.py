# https://www.codingame.com/training/easy/mars-lander-episode-1


def solution():
    surface_n = int(input())
    for i in range(surface_n):
        land_x, land_y = map(int, input().split())

    while True:
        x, y, h_speed, v_speed, fuel, rotate, power = list(map(int, input().split()))
        if abs(v_speed) > 36:
            print(0, min(4, power + 1))
        else:
            print(0, max(0, power - 1))


solution()

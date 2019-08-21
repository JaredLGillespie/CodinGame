# https://www.codingame.com/training/easy/temperatures


def solution():
    num_temps = int(input())
    closest_temp = float('inf')

    for temp in map(int, input().split()):
        if abs(temp) < abs(closest_temp):
            closest_temp = temp
        elif temp == -closest_temp:
            closest_temp = abs(closest_temp)

    print(closest_temp if num_temps != 0 else 0)


solution()

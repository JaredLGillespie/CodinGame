# https://www.codingame.com/training/easy/onboarding


def solution():
    while True:
        enemy1, dist1 = input(), int(input())
        enemy2, dist2 = input(), int(input())
        print(enemy1 if dist1 < dist2 else enemy2)


solution()

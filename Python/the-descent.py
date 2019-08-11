# https://www.codingame.com/training/easy/the-descent


def solution():
    while True:
        max_height = 0
        max_mountain = 0
        for i in range(8):
            height = int(input())
            if height > max_height:
                max_height = height
                max_mountain = i

        print(max_mountain)


solution()

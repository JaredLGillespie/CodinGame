# https://www.codingame.com/training/easy/power-of-thor-episode-1


def find_move(light_x, light_y, thor_x, thor_y):
    direction = ''
    change_x, change_y = 0, 0

    if thor_y < light_y:
        direction += 'S'
        change_y += 1
    elif thor_y > light_y:
        direction += 'N'
        change_y -= 1

    if thor_x < light_x:
        direction += 'E'
        change_x += 1
    elif thor_x > light_x:
        direction += 'W'
        change_x -= 1

    return direction, change_x, change_y


def solution():
    light_x, light_y, thor_x, thor_y = map(int, input().split())

    while True:
        remaining_turns = int(input())
        direction, change_x, change_y = find_move(light_x, light_y, thor_x, thor_y)
        thor_x, thor_y = thor_x + change_x, thor_y + change_y
        print(direction)


solution()

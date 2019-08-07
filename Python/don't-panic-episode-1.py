# https://www.codingame.com/training/medium/don't-panic-episode-1


def solution():
    num_floors, width, num_rounds, exit_floor, exit_pos, total_clones, _, num_elevators = map(int, input().split())

    elevators = [0] * num_floors
    for _ in range(num_elevators):
        floor, pos = map(int, input().split())
        elevators[floor] = pos

    elevators[exit_floor] = exit_pos

    while True:
        floor, pos, direction = input().split()
        floor, pos = int(floor), int(pos)

        if direction == 'LEFT':
            if pos >= elevators[floor]:
                print('WAIT')
            else:
                print('BLOCK')
        elif direction == 'RIGHT':
            if pos <= elevators[floor]:
                print('WAIT')
            else:
                print('BLOCK')
        else:
            print('BLOCK')


solution()

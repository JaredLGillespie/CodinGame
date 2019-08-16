# https://www.codingame.com/training/easy/simple-awale


def solution():
    op_bowls = list(map(int, input().split()))
    my_bowls = list(map(int, input().split()))
    bowl_index = int(input())

    grains = my_bowls[bowl_index]
    my_bowls[bowl_index] = 0
    bowl_index += 1
    while grains > 0:
        if bowl_index % 14 < 7:
            my_bowls[bowl_index % 7] += 1
            grains -= 1
        elif bowl_index % 14 < 13:
            op_bowls[bowl_index % 7] += 1
            grains -= 1
        bowl_index += 1

    print('{} [{}]'.format(' '.join(map(str, op_bowls[:-1])), op_bowls[-1]))
    print('{} [{}]'.format(' '.join(map(str, my_bowls[:-1])), my_bowls[-1]))
    if bowl_index == 7: print('REPLAY')


solution()

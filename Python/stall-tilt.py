# https://www.codingame.com/training/easy/stall-tilt


import math

STALL_ANGLE = 30


def min_bend_speed(bend):
    return int((math.tan(math.radians(90 - STALL_ANGLE)) * bend * 9.81) ** 0.5)


def find_optimal_speed(bends):
    return min(min_bend_speed(b) for b in bends)


def find_rankings(speeds, bends):
    active_racers = set(range(len(speeds)))
    min_bend_speeds = [min_bend_speed(b) for b in bends]
    rankings = []

    for mbs in min_bend_speeds:
        failed_racers = [r for r in active_racers if speeds[r] > mbs]
        for racer in sorted(failed_racers, key=lambda x: speeds[x]):
            active_racers.remove(racer)
            rankings.append(racer)

    for racer in sorted(active_racers, key=lambda x: speeds[x]):
        rankings.append(racer)

    return reversed(rankings)


def solution():
    num_motorcycles = int(input())
    num_curves = int(input())
    speeds = [int(input()) for _ in range(num_motorcycles)]
    bends = [int(input()) for _ in range(num_curves)]

    print(find_optimal_speed(bends))
    print('y')
    for m in find_rankings(speeds, bends):
        print(chr(m + ord('a')))


solution()

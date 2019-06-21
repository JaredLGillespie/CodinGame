# https://www.codingame.com/training/easy/bank-robbers


from heapq import *


def calc_vault_time(c, n):
    return 10**n * 5**(c - n)


def solution():
    robbers = int(input())
    vault = int(input())
    vault_times = []
    for i in range(vault):
        c, n = map(int, input().split())
        vault_times.append(calc_vault_time(c, n))

    active_robbers = []
    for vt in vault_times:
        if len(active_robbers) < robbers:
            heappush(active_robbers, vt)
        else:
            heappush(active_robbers, vt + heappop(active_robbers))

    print(max(active_robbers))

solution()

# https://www.codingame.com/training/easy/balanced-ternary-computer-encode


from collections import deque


def convert_system(num):
    if num in (0, 1):
        return str(num)
    return 'T'


def solution():
    n = int(input())

    if n in (0, 1, -1):
        print(convert_system(n))
        return

    queue = deque([(0, '0'), (1, '1'), (-1, 'T')])

    while True:
        val, bt = queue.popleft()

        for x in (0, 1, -1):
            nval = x * 3 ** len(bt) + val
            nbt = convert_system(x) + bt
            if nval == n:
                print(nbt)
                return
            queue.append((nval, nbt))


solution()

def meets_digital_river(r1, r2):
    return r1 == r2 + sum(map(int, str(r2)))


def solution():
    r1 = int(input())
    for r2 in range(max(1, r1 - 50), r1):
        if meets_digital_river(r1, r2):
            print('YES')
            break
    else:
        print('NO')


solution()

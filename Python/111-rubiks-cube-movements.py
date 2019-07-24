# https://www.codingame.com/training/easy/111-rubiks-cube-movements


def solution():
    rotations = input().split()
    face1, face2 = input(), input()
    F, B, U, D, L, R = 'FBUDLR'

    for rotation in rotations:
        if rotation[0] == 'x':
            if "'" in rotation: F, B, U, D = U, D, B, F
            else: F, B, U, D = D, U, F, B
        elif rotation[0] == 'y':
            if "'" in rotation: F, B, L, R = L, R, B, F
            else: F, B, L, R = R, L, F, B
        else:
            if "'" in rotation: U, D, L, R = R, L, U, D
            else: U, D, L, R = L, R, D, U

    loc = locals()
    print([x for x in loc if loc[x] == face1][0])
    print([x for x in loc if loc[x] == face2][0])


solution()

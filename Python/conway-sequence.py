# https://www.codingame.com/training/medium/conway-sequence


def solution():
    sequence = [int(input())]

    for _ in range(int(input()) - 1):
        prev_c, num_c = 0, 0
        new_sequence = []
        for c in sequence:
            if prev_c == 0:
                prev_c = c
                num_c = 1
            elif c == prev_c:
                num_c += 1
            else:
                new_sequence.append(num_c)
                new_sequence.append(prev_c)
                prev_c = c
                num_c = 1

        new_sequence.append(num_c)
        new_sequence.append(prev_c)
        sequence = new_sequence

    print(' '.join(map(str, sequence)))


solution()

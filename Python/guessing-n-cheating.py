# https://www.codingame.com/training/easy/guessing-n-cheating


def solution():
    num_rounds = int(input())
    rounds = [input().split() for _ in range(num_rounds)]
    answer = int(rounds[-1][0])
    l, r = 1, 100

    for n, rnd in enumerate(rounds):
        guess = int(rnd[0])
        reply = ' '.join(rnd[1:])

        if reply == 'too high':
            r = min(r, guess - 1)
        elif reply == 'too low':
            l = max(l, guess + 1)
        else:
            continue

        if l > r:
            print('Alice cheated in round {}'.format(n + 1))
            break

    else:
        if l <= answer <= r:
            print('No evidence of cheating')
        else:
            print('Alice cheated in round {}'.format(num_rounds))


solution()

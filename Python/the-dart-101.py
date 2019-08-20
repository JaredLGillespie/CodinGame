# https://www.codingame.com/training/easy/the-dart-101


TARGET_SCORE = 101


def simulate(shoots):
    rounds, throws, misses, score = 1, 0, 0, 0
    prev_round_score = 0
    prev_shot = ''
    for shot in shoots.split():
        throws += 1

        if 'X' in shot:
            misses += 1
            score -= 20
            if prev_shot == 'X': score -= 10
            if misses == 3: score = 0
            if throws == 3:
                throws = 0
                rounds += 1
                misses = 0
                prev_shot = ''
                prev_round_score = score
            else:
                prev_shot = shot
        else:
            if '*' in shot:
                a, b = map(int, shot.split('*'))
                points = a * b
            else:
                points = int(shot)

            if score + points == TARGET_SCORE:
                return rounds
            elif score + points > TARGET_SCORE:
                throws = 3
                score = prev_round_score
            else:
                score += points

            if throws == 3:
                throws = 0
                rounds += 1
                misses = 0
                prev_shot = ''
                prev_round_score = score
            else:
                prev_shot = shot

    return -1


def solution():
    num_players = int(input())
    player_names = [input() for _ in range(num_players)]
    shortest_rounds = float('inf')
    winner = ''

    for i in range(num_players):
        shoots = input()
        rounds = simulate(shoots)
        if rounds != -1 and rounds < shortest_rounds:
            shortest_rounds = rounds
            winner = player_names[i]

    print(winner)

solution()

# https://www.codingame.com/training/medium/winamax-battle


from collections import deque

card_values = {c: v for v, c in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])}


def solution():
    cards_1 = deque([input()[:-1] for _ in range(int(input()))])
    cards_2 = deque([input()[:-1] for _ in range(int(input()))])
    game_rounds = 0

    while cards_1 and cards_2:
        game_rounds += 1
        war_cards_1 = [cards_1.popleft()]
        war_cards_2 = [cards_2.popleft()]

        while card_values[war_cards_1[-1]] == card_values[war_cards_2[-1]]:
            for _ in range(4):
                if cards_1:
                    war_cards_1.append(cards_1.popleft())
                else:
                    print('PAT'); return
                if cards_2:
                    war_cards_2.append(cards_2.popleft())
                else:
                    print('PAT'); return

        if card_values[war_cards_1[-1]] > card_values[war_cards_2[-1]]:
            winner_cards = cards_1
        else:
            winner_cards = cards_2

        for card in war_cards_1 + war_cards_2:
            winner_cards.append(card)

    if cards_1:
        print('1 {}'.format(game_rounds))
    else:
        print('2 {}'.format(game_rounds))


solution()

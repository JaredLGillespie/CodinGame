# https://www.codingame.com/ide/puzzle/hunger-games


def solution():
    num_tributes = int(input())
    tributes = {input(): {'killer': 'Winner', 'killed': []} for _ in range(num_tributes)}
    turns = int(input())
    for _ in range(turns):
        name, _, *victims = input().split()
        for victim in [v.replace(',', '') for v in victims]:
            tributes[name]['killed'].append(victim)
            tributes[victim]['killer'] = name

    for i, tribute in enumerate(sorted(tributes)):
        if i != 0: print()
        print('Name: {}'.format(tribute))
        victims = tributes[tribute]['killed']
        if not victims: print('Killed: None')
        else: print('Killed: {}'.format(', '.join(sorted(victims))))
        print('Killer: {}'.format(tributes[tribute]['killer']))


solution()

# https://www.codingame.com/training/easy/brackets-extreme-edition


def solution():
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in input():
        if c in '([{':
            stack.append(pairs[c])
        elif c in ')]}':
            if not stack or stack[-1] != c:
                print('false')
                return

            stack.pop()

    print('true' if not stack else 'false')


solution()

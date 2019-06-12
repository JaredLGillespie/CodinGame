# https://www.codingame.com/training/easy/ascii-art


def get_ascii_map_index(char):
    if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return 26

    return ord(char) - ord('A')


def solution():
    width = int(input())
    height = int(input())
    text = input()

    ascii_map = [[] for _ in range(27)]

    for _ in range(height):
        line = input()
        for i in range(27):
            ascii_map[i].append(line[i * width:i * width + width])

    for col in range(height):
        for char in text.upper():
            part = ascii_map[get_ascii_map_index(char)][col]
            print('{}'.format(part), end='')
        print()


solution()

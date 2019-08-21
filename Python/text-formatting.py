# https://www.codingame.com/training/easy/text-formatting


import string

VALID_CHARACTERS = set(string.ascii_letters + string.digits)


def parse(text):
    prev_char = ''
    for c in text.lower():
        if prev_char == '':
            if c in VALID_CHARACTERS:
                prev_char = c.upper()

        elif c in VALID_CHARACTERS:
            if prev_char in VALID_CHARACTERS or prev_char == ' ':
                yield prev_char
                prev_char = c
            elif prev_char in ',;':
                yield prev_char + ' '
                prev_char = c
            else:
                yield prev_char + ' '
                prev_char = c.upper()

        elif c == ' ':
            if prev_char in VALID_CHARACTERS:
                yield prev_char
                prev_char = c

        else:
            if prev_char in VALID_CHARACTERS:
                yield prev_char
            prev_char = c

    if prev_char != ' ':
        yield prev_char


def solution():
    print(''.join(parse(input())))


solution()

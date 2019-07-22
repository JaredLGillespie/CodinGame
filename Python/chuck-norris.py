def print_conversion(prev_char, cur_count, first_char):
    space = '' if first_char else ' '

    if prev_char == '0':
        print('{}00 {}'.format(space, '0' * cur_count), end='')
    else:
        print('{}0 {}'.format(space, '0' * cur_count), end='')


def solution():
    binary = []
    for char in input():
        binary.extend('{:b}'.format(ord(char)).zfill(7))

    prev_char = None
    cur_count = 0
    first_char = True
    for x in binary:
        if prev_char is None:
            prev_char = x
            cur_count += 1
        elif prev_char == x:
            cur_count += 1
        else:
            print_conversion(prev_char, cur_count, first_char)
            first_char = False
            prev_char = x
            cur_count = 1

    print_conversion(prev_char, cur_count, first_char)


solution()

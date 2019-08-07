# https://www.codingame.com/training/medium/telephone-numbers


def add_number(number, directory):
    elements = 0
    for digit in number:
        if digit not in directory:
            directory[digit] = {}
            elements += 1
        directory = directory[digit]

    return elements


def solution():
    elements = 0
    directory = {}
    for _ in range(int(input())):
        elements += add_number(input(), directory)

    print(elements)


solution()

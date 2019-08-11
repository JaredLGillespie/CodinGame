# https://www.codingame.com/training/easy/mime-type


def solution():
    num_elements = int(input())
    num_files = int(input())

    association_table = {}

    for _ in range(num_elements):
        ext, mt = input().split()
        association_table[ext.lower()] = mt

    for _ in range(num_files):
        fileparts = input().split('.')
        if len(fileparts) == 1:
            print('UNKNOWN')
            continue

        ext = fileparts[-1].lower()
        if ext in association_table:
            print(association_table[ext])
        else:
            print('UNKNOWN')


solution()

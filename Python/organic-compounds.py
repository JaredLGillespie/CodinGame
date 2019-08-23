# https://www.codingame.com/training/easy/organic-compounds


def check_for_bond(row, col, formula):
    if row < 0 or row >= len(formula): return 0
    if col < 0 or col >= len(formula[row]): return 0
    return int(formula[row][col]) if formula[row][col] in '0123' else 0


def sum_bonds(row, col, formula):
    return check_for_bond(row, col - 2, formula) + \
           check_for_bond(row, col + 4, formula) + \
           check_for_bond(row - 1, col + 1, formula) + \
           check_for_bond(row + 1, col + 1, formula)


def solution():
    formula = [input() for _ in range(int(input()))]

    for row in range(len(formula)):
        for col in range(len(formula[row])):
            if formula[row][col] == 'C':
                carbon_units = int(formula[row][col + 2])
                bonds = sum_bonds(row, col, formula)
                if carbon_units + bonds != 4:
                    print('INVALID')
                    return

    print('VALID')


solution()

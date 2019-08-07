# https://www.codingame.com/training/easy/bulk-email-generator


def solution():
    text = '\n'.join(input() for _ in range(int(input())))

    clause_choice = 0
    output = []
    index = 0
    clause_index = 0
    in_clause = False

    while index < len(text):
        c = text[index]
        if c == '(':
            in_clause = True
            clause_index = index
        elif c == ')':
            in_clause = False
            if clause_index + 1 == index:
                index += 1
                continue

            clauses = text[clause_index + 1:index].split('|')
            output.append(clauses[clause_choice % len(clauses)])
            clause_choice += 1
        elif in_clause:
            index += 1
            continue
        else:
            output.append(c)
        index += 1

    print(''.join(output))


solution()

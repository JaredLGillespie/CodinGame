def is_valid_isbn(isbn):
    if len(isbn) not in (10, 13): return False
    if 'X' in isbn[:-1]: return False
    if len(isbn) == 10: return is_valid_isbn10(isbn)
    return is_valid_isbn13(isbn)


def is_valid_isbn10(isbn):
    w = 10
    s = 0
    for d in isbn[:-1]:
        s += w * int(d)
        w -= 1

    if s % 11 == 0: return isbn[-1] == '0'
    if s % 11 == 1: return isbn[-1] == 'X'
    if isbn[-1] == 'X': return False
    return int(isbn[-1]) == 11 - s % 11


def is_valid_isbn13(isbn):
    w = 1
    s = 0
    for d in isbn[:-1]:
        s += w * int(d)
        w ^= 2

    if s % 10 == 0: return isbn[-1] == '0'
    if isbn[-1] == 'X': return False
    return int(isbn[-1]) == 10 - s % 10


def solution():
    num_isbns = int(input())
    invalid_isbns = []

    for _ in range(num_isbns):
        isbn = input()
        if not is_valid_isbn(isbn):
            invalid_isbns.append(isbn)

    print('{} invalid:'.format(len(invalid_isbns)))
    for isbn in invalid_isbns:
        print(isbn)


solution()

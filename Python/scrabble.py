# https://www.codingame.com/training/medium/scrabble


from collections import Counter

letter_weights = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}


def can_make_word(word, letters):
    word_counter, letters_counter = Counter(word), Counter(letters)
    if any(c for c in word if c not in letters): return False
    for c in word_counter:
        if c not in letters_counter: return False
        if word_counter[c] > letters_counter[c]: return False
    return True


def get_word_score(word):
    return sum(letter_weights[c] for c in word)


def solution():
    words = [input() for _ in range(int(input()))]
    letters = input()
    max_word_score = 0
    max_word = ''

    for word in words:
        if not can_make_word(word, letters): continue
        word_score = get_word_score(word)
        if word_score > max_word_score:
            max_word_score = word_score
            max_word = word

    print(max_word)


solution()

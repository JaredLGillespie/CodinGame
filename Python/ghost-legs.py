# https://www.codingame.com/training/easy/ghost-legs


def find_path(current_index, levels, h, w):
    for level_index in range(h - 2):
        level = levels[level_index]
        if current_index == 0:
            if level[current_index + 1] == '-':
                current_index += 3
        elif current_index == w - 1:
            if level[current_index - 1] == '-':
                current_index -= 3
        else:
            if level[current_index + 1] == '-':
                current_index += 3
            elif level[current_index - 1] == '-':
                current_index -= 3
    return current_index


def solution():
    w, h = map(int, input().split())

    top_labels = None
    bottom_labels = None
    levels = []

    for i in range(h):
        if i == 0:
            top_labels = input().split()
        elif i == h - 1:
            bottom_labels = input().split()
        else:
            levels.append(list(input()))

    for top_index, top_label in enumerate(top_labels):
        bottom_index = find_path(top_index * 3, levels, h, w) // 3
        bottom_label = bottom_labels[bottom_index]
        print('{}{}'.format(top_label, bottom_label))


solution()

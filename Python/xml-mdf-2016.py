# https://www.codingame.com/training/easy/xml-mdf-2016


def solution():
    depth = 1
    tag_weights = {}
    skip = False

    for c in input():
        if skip:
            skip = False
        elif c == '-':
            depth -= 1
            skip = True
        else:
            if c not in tag_weights:
                tag_weights[c] = 0
            tag_weights[c] += 1 / depth
            depth += 1

    max_tag = ''
    max_weight = 0

    for tw in tag_weights:
        if tag_weights[tw] > max_weight:
            max_weight = tag_weights[tw]
            max_tag = tw
        elif tag_weights[tw] == max_weight and tw < max_tag:
            max_weight = tag_weights[tw]
            max_tag = tw

    print(max_tag)


solution()

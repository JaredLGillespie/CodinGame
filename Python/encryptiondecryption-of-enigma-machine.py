# https://www.codingame.com/training/easy/encryptiondecryption-of-enigma-machine


def forward_ceasar(ceasar_shift, message):
    ret = []
    for c in message:
        ret.append(chr((ord(c) - ord('A') + ceasar_shift) % 26 + ord('A')))
        ceasar_shift = (ceasar_shift + 1) % 26
    return ''.join(ret)


def reverse_ceasar(ceasar_shift, message):
    ceasar_shift = (ceasar_shift + len(message) - 1) % 26
    ret = []
    for c in reversed(message):
        ret.append(chr((ord(c) - ord('A') - ceasar_shift) % 26 + ord('A')))
        ceasar_shift = (ceasar_shift - 1) % 26
    return ''.join(reversed(ret))


def forward_rotor(rotor, message):
    return ''.join(rotor[ord(c) - ord('A')] for c in message)


def reverse_rotor(rotor, message):
    reverse_map = {c: i for i, c in enumerate(rotor)}
    return ''.join(chr(reverse_map[c] + ord('A')) for c in message)


def encode(ceasar_shift, rotors, message):
    message = forward_ceasar(ceasar_shift, message)
    for rotor in rotors:
        message = forward_rotor(rotor, message)
    return message


def decode(ceasar_shift, rotors, message):
    for rotor in reversed(rotors):
        message = reverse_rotor(rotor, message)
    message = reverse_ceasar(ceasar_shift, message)
    return message


def solution():
    operation = input()
    ceasar_shift = int(input())
    rotors = [input() for _ in range(3)]
    message = input()

    if operation == 'ENCODE':
        print(encode(ceasar_shift, rotors, message))
    else:
        print(decode(ceasar_shift, rotors, message))


solution()

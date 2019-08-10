# https://www.codingame.com/training/easy/whats-so-complex-about-mandelbrot


def solution():
    c = complex(input().replace('i', 'j'))
    fn = 0
    for i in range(1, int(input()) + 1):
        fn = fn**2 + c
        if abs(fn) > 2: break
    print(i)


solution()

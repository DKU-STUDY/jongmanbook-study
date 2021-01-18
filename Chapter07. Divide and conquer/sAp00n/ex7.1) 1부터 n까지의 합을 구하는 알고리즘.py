from sys import stdin
from random import randint


def fast_sum(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return fast_sum(n - 1) + n
    return fast_sum(n/2) + fast_sum(n/2) + (n/2 * n/2)


print('Input number n(1 ~ 5000)\nIf you just press enter random number will be chosen')
input_str = stdin.readline()

if input_str == '\n':
    n = randint(1, 5000)
    print(f'Random number {n} is chosen')
else:
    n = int(input_str)
    print(f'Number {n} has been entered')

print(f'result: {int(fast_sum(n))}')

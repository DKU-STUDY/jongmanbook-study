from sys import stdin
from random import randint


# 초등학교 알고리즘

def elementary_mult(a, b):
    longer_num, shorter_num = max(a, b), min(a, b)
    longer_num, shorter_num = str(longer_num), str(shorter_num)
    longer_num_len, shorter_num_len = len(longer_num), len(shorter_num)
    computing_que = [[0] * longer_num_len for i in range(shorter_num_len)]

    for idx in range(shorter_num_len - 1, -1, -1):
        current_numi = shorter_num[idx]
        for jdx in range(longer_num_len - 1, -1, -1):
            current_numj = longer_num[jdx]
            computing_que[shorter_num_len - 1 - idx][longer_num_len - 1 - jdx] = int(current_numi) * int(current_numj)

    total_sum = 0
    for i in range(len(computing_que)):
        for j in range(len(computing_que[i])):
            temp = (computing_que[i][j] * (pow(10, i))) * pow(10, j)
            total_sum += temp
    return total_sum


def karatsuba_mult(a, b):
    a, b = str(a), str(b)
    if len(b) > len(a):
        a, b = b, a

        diff = len(a) - len(b)
        b = '0' * diff + b
    if a == 0 or b == 0:
        return 0
    if len(a) < 50:
        return elementary_mult(a, b)

    a1, a0 = a[:len(a) // 2], a[len(a) // 2:]
    b1, b0 = b[:len(b) // 2], b[len(b) // 2:]
    z2 = karatsuba_mult(a1 * b1)
    z0 = karatsuba_mult(a0, b0)
    z1 = karatsuba_mult((a0 + a1) * (b0 + b1)) - z0 - z2
    total_sum = int(z2 + '0' * len(a) // 2) + int(z1 + '0' * len(a) // 4) + z0
    return total_sum


a, b = randint(1000, 1000000000), randint(1000, 1000000000)
result = elementary_mult(a, b)
kara_result = karatsuba_mult(a, b)
print(f'ele => {a} * {b} = {result}  check: {result == a * b}\nkara => {a} * {b} = {kara_result}   check: {kara_result == a * b}')

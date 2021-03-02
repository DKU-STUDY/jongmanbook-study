from sys import stdin


def fractal_plane(location, s, N, K):
    x, y = location
    if y == 1:
        temp = 0
    leng = N**s
    unit = leng / N
    border = (N - K) /2
    while unit > 0:
        if border <= y // unit <= N - 1 - border and border <= x // unit <= N - 1 - border:
            #print(f'({x}, {y}) in')
            return '1'
        if y >= unit:
            y %= unit
        if x >= unit:
            x %= unit
        unit /= N
    return '0'


s, N, K, R_1, R_2, C_1, C_2 = map(int, stdin.readline().split())


for y in range(R_1, R_2 + 1):
    line = ''
    for x in range(C_1, C_2 + 1):
        line += fractal_plane((x, y), s, N, K)
    print(line)

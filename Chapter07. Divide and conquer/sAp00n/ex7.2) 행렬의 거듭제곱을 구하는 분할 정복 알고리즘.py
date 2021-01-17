from random import randint


def mat_mult(mat01, mat02):
    len_of_mat = len(mat01)
    return_mat = [[0] * len_of_mat for i in range(len_of_mat)]
    for i in range(len_of_mat):
        for j in range(len_of_mat):
            temp = 0
            row = mat01[i]
            for k in range(len_of_mat):
                temp += row[k] * mat02[k][j]
            return_mat[i][j] = temp
    return return_mat


def mat_pow(mat, n):
    if n == 1:
        return mat
    if n // 2 == 1:
        return mat_mult(mat_pow(mat, n - 1), mat)
    return mat_mult(mat_pow(mat, n // 2), mat_pow(mat, n // 2))


size_of_mat = randint(2, 2)
mat = [[randint(0, 10) for j in range(size_of_mat)] for i in range(size_of_mat)]

for column in mat:
    print(column)

n = randint(1, 50000)
print(f'n: {n}\n')
computed_mat = mat_pow(mat, n)

for row in computed_mat:
    print(row)

"""
BOJ 2751 수 정렬하기 2 예제로 연습
"""

from sys import stdin
from random import randint

input_txt = stdin.readline()
boj_mode = False
if input_txt != '\n':
    boj_mode = True
    input_list = [int(stdin.readline()) for i in range(int(input_txt))]
else:
    input_list = [randint(1, 99) for i in range(randint(5, 30))]
    print(f'input list: {input_list}')


# 병합정렬
def merge_sort(input_list):
    len_of_list = len(input_list)
    if len_of_list > 2:
        return merge(merge_sort(input_list[:len_of_list // 2]), merge_sort(input_list[len_of_list // 2:]))
    if len_of_list == 2:
        return [min(input_list), max(input_list)]
    return input_list


def merge(list01, list02):
    i_max, j_max, i, j = len(list01), len(list02), 0, 0
    sorted_list = []
    while i <= i_max and j <= j_max:
        if i == i_max and j == j_max:
            i += 1
            j += 1
            continue
        if i == i_max:
            sorted_list.append(list02[j])
            j += 1
            continue

        if j == j_max:
            sorted_list.append(list01[i])
            i += 1
            continue

        if list01[i] > list02[j]:
            sorted_list.append(list02[j])
            j += 1
            continue

        sorted_list.append(list01[i])
        i += 1
        continue
    return sorted_list


sorted_list = merge_sort(input_list)

if boj_mode:
    for ele in sorted_list:
        print(ele)

else:
    print(f'sorted_list: {sorted_list}')
"""
BOJ 2751 수 정렬하기 2 예제로 연습
"""

from sys import stdin
from random import randint

input_txt = stdin.readline()
boj_mode = False
quick_or_merge = False
if input_txt != '\n':
    boj_mode = True
    input_list = [int(stdin.readline()) for i in range(int(input_txt))]
else:
    input_list = [randint(1, 99) for i in range(randint(5, 3000))]
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


# 퀵 정렬
def quick_sort(input_list):
    len_of_list = len(input_list)
    if len_of_list == 2:
        return [min(input_list), max(input_list)]
    if len_of_list <= 1:
        return input_list

    pivot = input_list[0]

    list01, list02 = [], []
    for i in range(1, len_of_list):

        if input_list[i] < pivot:
            list01.append(input_list[i])
        else:
            list02.append(input_list[i])

    return quick_sort(list01) + [pivot] + quick_sort(list02)


if boj_mode:
    if quick_or_merge:
        sorted_list = merge_sort(input_list)
    else:
        sorted_list = quick_sort(input_list)

    for ele in sorted_list:
        print(ele)

else:
    print(f'merge_list: {merge_sort(input_list)}')
    print(f'quick_sort: {quick_sort(input_list)}')

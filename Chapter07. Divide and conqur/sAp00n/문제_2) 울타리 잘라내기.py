"""
N 개의 늘어져 있는 각자 다른높이의 울타리에서 잘라낼 수 있는 가장 큰 넓이를 구하는 문제.

N = 2 * 10^4
시간제한은 1sec 이므로,
1 * 10^8 / 2 * 10^4(N) = 대락 O(N^2)복잡도 이하로 작성되어야 한다

하지만.... O(N!*N) 밖에 생각나지 않는다..

"""

from sys import stdin


def computed_max(list_of_fence, left, right):

    if left == right:
        return list_of_fence[left]

    mid_idx = (left + right) // 2

    result = max(computed_max(list_of_fence, left, mid_idx), computed_max(list_of_fence, mid_idx + 1, right))
    lo, hi = mid_idx, mid_idx + 1
    height = min(list_of_fence[lo], list_of_fence[hi])
    result = max(result, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or list_of_fence[lo - 1] < list_of_fence[hi + 1]):
            hi += 1
            height = min(height, list_of_fence[hi])
        else:
            lo -= 1
            height = min(height, list_of_fence[lo])

        result = max(result, height * (hi - lo + 1))

    return result


C = int(stdin.readline())  # test case 의 개수

for i in range(C):
    N = int(stdin.readline())  # 판자의 개수
    list_of_fence = list(map(int, stdin.readline().split()))
    print(computed_max(list_of_fence, 0, N - 1))

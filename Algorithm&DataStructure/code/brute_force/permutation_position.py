"""
재귀 호출 + 최소 횟수로 원소 교환을 이용한

순열 생성
"""

a = [1, 2, 3, 4, 5]
n = len(a)


def perm(a, n, k):
    if k == n:
        print(a)
    for i in range(k, n):
        a[k], a[i] = a[i], a[k]
        perm(a, n, k + 1)
        a[k], a[i] = a[i], a[k]


perm(a, n, 0)

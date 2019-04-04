# 분할 정복 (Divide & Conquer)

1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이

연합군의 중앙으로 쳐들어가서 연합군을 둘로 `분할`하여 각각을 격파(`정복`)하여 승리한데서 유래했습니다.



## 분할 정복 기법

### 거듭제곱

시간 복잡도 : O(logn)

```python
def power_recursive(n, r):
    if r == 1:
        return n
    elif r % 2 == 0:
        y = power_recursive(n, r // 2)
        return y * y
    elif r % 2 == 1:
        y = power_recursive(n, r // 2)
        return y * y * n
```



### 병합정렬

시간 복잡도 : O(nlogn)

```python
def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. DIVIDE
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # list 크기를 1로 만들기
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER : 분할된 리스트 병합
    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)

    if len(right) > 0:
        result.extend(right)

    return result


print(merge_sort([4, 7, 3, 3, 6, 3, 1, 9]))
```





### 퀵 정렬 (Quick Sort)

```python
def hoare_partition(A, l, r):
    """Hoare-Partition"""
    pivot = A[l]
    i, j = l + 1, r
    while i <= j:
        while i <= j and A[i] < pivot: i += 1
        while i <= j and A[j] > pivot: j -= 1
        if i <= j: A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def lomuto_partition(A, l, r):
    """Lomuto-partition"""
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quick_sort(A, l, r, partition=hoare_partition):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s-1, partition=partition)
        quick_sort(A, s+1, r, partition=partition)


li = [1, 5, 6, 4, 2, 7]
quick_sort(li, 0, 5, partition=lomuto_partition)
print(li)
```




# 백트래킹 (BackTracking)

- 해를 찾는 도중에 해가 아니면 되돌아가서 다시 해를 찾아가는 기법
  1. 여러가지 선택지가 존재하는 상황에서 한가지 선택
  2. 선택이 이뤄지면 새로운 선택지들의 집합 생성
  3. 선택을 반복하면서 최종 상태에 도달

- 최적화(Optimization) 문제와 결정 문제를 해결할 수 있음

> 결정문제 : 문제의 조건을 만족하는 해가 존재하는지 여부를 답하는 문제

- 최적화
  - 부분 집합의 합 중 원소의 개수가 최대인 것
- 결정문제
  - 미로찾기 (출구까지 경로, 원소의 합이 조건에 맞는지, 최단 경로)
  - n-Queens
  - Map coloring
  - 부분 집합의 합

- pseudo code

```python
def checknode(v):
    if promising(v):
        if v is solution:
            return v
        else:
            for u in v.get_childs():
                checknode(u)
```



## 예제

### subset

```python
def subset(a, k, n):
    if k == n:
        # process_solution(a, n)
        print(a)
    else:
        a[k] = 0
        subset(a, k+1, n)
        a[k] = 1
        subset(a, k+1, n)


subset([0, 1, 2], k=0, n=3)
```


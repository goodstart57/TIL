# 동적 계획법(DP; Dynamic Programming)

## 메모이제이션(Memoization)

글자 그대로 해석하면 `메모리에 넣기`라는 의미로 이전에 수행했던 결과를 저장하여 같은 연산을 반복하지 않음으로써 수행 시간을 줄이는 것으로 동적 계획법(DP; Dynamic Programming)의 핵심 기술



## 동적 계획법

`분할 정복 알고리즘과` 비슷한 `DP`는 `메모이제이션`을 사용하여 주어진 문제를 부분 문제로 나누어서 각 부분 문제의 답을 저장하여 같은 연산을 수행해야하는 경우의 연산량을 줄일 수 있다.



### 동적 계획법의 접근법

- 재귀 함수 (recursive)
- 반복문 (iterative)



### Python Code Fibonacci Example

#### 재귀 (recursive)

```python
def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n-1) + fibo1(n-2)
fibo1(10)
```

재귀로 함수를 정의하는 경우 함수 호출시 프로그램의 메모리 스택에 데이터가 쌓이게 되어 연산 횟수가 늘어나는 경우 스택오버플로우가 발생하게 된다.



#### 동적 계획법을 활용한 피보나치 수열

```python
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
fibo(10)
```


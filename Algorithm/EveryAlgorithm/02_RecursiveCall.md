# 모두의 알고리즘 with 파이썬 - Chapter02 재귀호출

함수가 자기 자신을 다시 호출하는 것을 의미

익숙해지면 프로그램을 매우 빠르게 짤 수 있다.

## 연습문제

### 팩토리얼(factorial)

```python
def normal_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)
```

### 최대공약수(Greatest Common Divisor, GCD)

```python
def normal_GCD(a, b):
    for i in range(a if a < b else b, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

def recursive_GCD(a, b):
    if b == 0:
        return a
    elif a == b:
        return a
    elif a < b:
        return recursive_GCD(a, b % a)
    elif b < a:
        return recursive_GCD(b, a % b)
```


### 하노이의탑

```python
'''하노이의 탑
[입력]
n : 옮기려는 원반의 개수
pos_s : 출발점 기둥 위치
pos_e : 도착점 기둥 위치
pos_a : 보조 기둥 위치

[출력]
원반을 옮기는 순서
'''

def hanoi(n, pos_s, pos_e, pos_a):
    if n==1:
        print(f"[{n}]{pos_s}-({pos_a})->{pos_e}")
        return

    hanoi(n-1, pos_s, pos_a, pos_e)
    print(f"[{n}]{pos_s}-({pos_a})->{pos_e}")
    hanoi(n-1, pos_a, pos_e, pos_s)

print("n=4")
hanoi(4, 1, 3, 2)
print()
```
# 재귀 Recursive

재귀는 `원래의 자리로 되돌아가거나 되돌아옴`이라는 뜻으로 함수를 정의할 때 자기 자신을 호출하여 자기 자신을 재 참조하는 방법으로 많이 사용한다.



## 재귀함수의 장단점

### 장점

1. 재귀함수로 표현할 때 가독성이 좋은 알고리즘이 있다. (소스코드의 길이가 짧아진다.)
2. 변수 사용을 줄여준다.

### 단점

1. 메모리를 많이 차지하여 성능이 반복문에 비하여 느리다.

=> 함수 호출 시 함수의 매개변수, 지역변수, 리턴 값, 함수 종료 후 돌아가는 위치가 스택 메모리에 저장되는데, 재귀함수 호출 시 함수를 계속해서 호출해서 스택 메모리가 커져서 스택오버플로우가 발생하는 경우가 많다.



## 재귀 함수 예제: 피보나치 수열

```
f(0) = 1, f(1) = 1
f(i) = f(i - 1) + f(i - 2)
```

위 피보나치 수열의 패턴을 코드로 나타내면 아래와 같다.



```python
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```


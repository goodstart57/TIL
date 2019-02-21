# 자료구조 (Data Structure)

많이 사용하는 자료의 논리 구조를 정형화시켜서 범용적으로 사용하는 형태



## ADT (Abstract Data Type)

추상적 자료형으로 구현 방법을 명시하지 않는다는 점과 각 연산의 시간 복잡도를 명시하지 않는 점에서 자료구조와 달리한다.

**구조** (결국 클래스 구조)

연산 후에 논리 구조가 흐트러지면 안된다.

**연산**



## 스택 (stack)

물건을 쌓아 올리듯 자룟를 쌓아 올린 형태의 자료구조

`선형 구조` : 자료간의 관계가 1대 1의 관계를 갖는다. (비선형은 1:N의 관계)

`LIFO (Last-In-First-Out)` : 마지막에 삽입한 자료를 가장 먼저 꺼낸다.



### 스택의 구현

스택의 삽입/삭제

![stack-operation](C:\Workspace\ssafy-algorithm\image\stack-operation.png)



### 스택의 응용1: 괄호 검사

괄호의 종류 : 대/중/소 괄호 ("[]", "{}", "()")

**제한조건**

왼쪽 괄호 개수 == 오른쪽 관호 개수

같은 괄호에서 왼쪽 괄호는 오른쪽 보다 먼저 나와야한다.

괄호 사이에는 포함 관계만 존재한다.

**스택을 이용한 괄호 검사 과정**

1. 시작 괄호 insert
2. 닫는 괄호 pop

erro) 괄호 수식이 끝났는데 스택에 괄호가 남아있음

![stack-ex-bracket](C:\Workspace\ssafy-algorithm\image\stack-ex-bracket.png)

**Python Code**

```python
problem = ["()()((()))", "((()((((()()((()())((())))))"]

for TCN, brackets in enumerate(problem, 1):
    li = [0] * 100
    top, result = -1, True
    for b in brackets:
        if b == "(":
            top = top + 1
            li[top] = b
        elif b == ")":
            if li[top] != "(":
                result = False
                break
            li[top], top = 0, top - 1
    print("#{} {}".format(TCN, result))
```

```
#1 True
#2 True
```

### 스택의 응용: 후위표기법

```
중위표기법(infix notation)
연산자를 피연산자의 가운데 표기하는 방법 ( 1 + 2 )

후위 표기법(postfix notation)
연산자를 피연산자 뒤에 표기하는 방법 ( 1 2 + )
```

```python
idx = 0
post_exp = [0] * 10

for i in range(len(string)):
    if '*' <= str[i] <= '/':
        top += 1:
        stack[top] = string[i]
    elif '0' <= string[i] <= '9':
        post_exp[idx] = string[i]
        idx += 1
while top != -1:
    post_exp[idx] = stack[top]
    idx += 1
    top -= 1
print(' '.join(post_exp[:idx]))
```



## 스택 - 백트래킹 Backgracking

해를 찾는 도중에 해가 아니면 되돌아가서 다시 해를 찾아가는 기법

`최적화 문제`와 `결정 문제`를 해결할 수 있다.

### DFS와 백트래킹의 차이?

DFS : 비선형 자료구조의 `모든 자료`를 순회할 수 있는 로직

백트래킹 : DFS와 달리 `Prunning`을 통해서 어떤 경로가 해결책으로 이어질 것 같지 않으면 그 경로를 탐색하지 않는다.

### 백트래킹 기법

1. 어떤 노드의 유망성을 점검하여 유망(promising) 하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 간다.

### 결정문제

문제의 조건을 만족하는 해가 존재하는지의 여부를 답하는 문제

- 미로 찾기
- n-Queen
- Map coloring
- 부분집합의 합







## 그래프

이진트리, 이진탐색트리, 인덱스트리, 허프만 트리 등등

최단경로 - BFS, 다엑스트라 등등

### 순회 

1. in-order
2. pre-order
3. post-order

### 순회 두가지 방법

#### 깊이 우선 탐색 (Depth First Search, DFS)

시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복해야 하므로 후입 선출 구조의 `스택` 사용

1) 시작 노드 v를 결정하여 방문

2) 노드 v에 인접한(adjacent) 노드 중에서 

1. 방문하지 않은 노드 w가 있으면 노드 v를 스택에 push하고 노드 w에 방문하고 w를 v로 하여 다시 2)를 반복한다.

2. 방문하지 않은 정점이 없으면 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복

3) 스택이 공백이 될 때 까지 2)를 반복



#### 너비 우선 탐색 (Breadth First Search, BFS) -- Queue




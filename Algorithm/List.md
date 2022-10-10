# List

순서를 가진 데이터의 집합을 가리키는 추상 자료형

- 순차 리스트 -- 배열을 기반으로 구현된 리스트
- 연결 리스트 -- 메모리의 동적 할당을 기반으로 구현된 리스트

>  파이썬의 리스트와는 다른 의미



## 순차 리스트

1차원 배열에 항목들을 순서대로 저장

데이터의 종류와 구조에 따라서 구조화된 자료구조를 만들어 배열로 만들 수 있다.

### 순차 리스트의 문제점

- 배열을 이용하기 때문에 자료의 삽입/삭제 연산과정에서 연속적인 메모리 배열을 위해서 원소를 이동시키는 작업이 필요하다.
- 배열의 크기가 정해져있는 경우 메모리 낭비
- 할당된 메모리보다 많은 자료를 사용해야하기 때문에 새롭게 배열을 만들어야할 수 있다.



## 연결 리스트

자료의 논리적인 순서와 메모리상의 물리적인 순서가 일치하지 않고,

개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.

링크를 통해 원소에 접근하므로, 순차리스트에서처럼 물리적인 순서를 맞추기 위한 작업이 필요하지않다.

자료구조의 크기가 동적으로 조정할 수 있어서 메모리의 효율적인 사용이 가능하다.

### 연결 리스트의 기본 구조

#### 노드

연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료단위로 데이터필드와 링크 필드를 가지고 있다.

데이터 필드 -- 저장할 Element에 따라서 값을 가질수도 있고 원하는 자료 구조를 만들어 저장할 수 있다.

링크 필드 -- 다음 노드의 주소를 저장

#### 헤드

리스트의 처음 노드를 가리키는 레퍼런스

### 

### 단순 연결 리스트(Singly Linked List)

#### 연결 구조

- `헤드`가 가장 앞의 노드를 가리킨다.

- 노드의 `링크 필드`에 `다음 노드의 주소를 저장`하여 다음 노드와 연결되는 구조를 가진다.
- 마지막 노드는 `NULL(None)`을 가리킨다.

#### 단순 연결 리스트의 삽입 연산

1. 새로운 노드 `new` 생성, 데이터 필드에 `B` 저장
2. 삽입될 위치의 앞 노드의 링크 필드를 new의 링크 필드에 저장
3. new의 주소를 앞 노드의 링크 필드에 저장

#### 단순 연결 리스트 구현

```python
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_to_first(self, data):
        self.head = Node(data)
    
    def add(self, pre, data):
        if pre == None:
            print('error')
        else:
            pre.link = Node(data, pre.link)
        
    def add_to_last(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            p = self.head
            while p.link != None:
                p = p.link
            p.link = Node(data)
    
    def delete(self, pre):
        """delete pre.link"""
        if pre == None or pre.link == None:
            print('error')
        else:
            pre.link = pre.link.link
    
    def print(self):
        p = self.head
        while p.link != None:
            print(f'[{p.data}|{id(p.link)}]-', end="")
            p = p.link
        print(f'[{p.data}|{id(p.link)}]')

sll = SinglyLinkedList()
sll.add_to_first(1)
sll.add(sll.head, 2)
sll.add_to_last(3)
sll.print()
sll.delete(sll.head)
sll.print()
```

```
[1|2338387790984]-[2|2338387791376]-[3|140715044981984]
[1|2338387791376]-[3|140715044981984]
```


# Python

## Memory Management about append

```python
import time

st = time.time()
loo = 100000000
s = []
for i in range(loo):
    s.append(i)

print("append :", time.time() - st)
```

```
append : 14.33965802192688
```



```python
import time

st = time.time()
loo = 100000000
s = [0] * loo
for i in range(loo):
    s[i] = i

print("+ opertate :", time.time() - st)
```

```
+ opertate : 7.856065988540649
```



append를 사용하는 경우 메모리를 재할당해야 해서 append 사용 횟수가 늘어나는 경우 오버플로우가 일어날 수 있다.

따라서 사용할 공간을 미리 할당받아서 사용함으로써 메모리 관리를 할 수 있다.
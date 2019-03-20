# How to write log in Python

## 1. logging

[logging tutorial in my github](https://github.com/goodstart57/TIL/blob/master/Python/logging-tutorial.ipynb)



## 2. stdout

```python
import sys

sys.stdout = open('output.txt', 'w')
```

sys의 stdout과 open 함수를 이용해서 원하는 경로의 파일에 로그를 남길 수 있다.


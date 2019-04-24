# Non-blocking Property

## Diff between Python and JavaScript

### blocking (Python)

중간에 sleep이 들어가면 sleep에서 빠져나올 때 까지 막혀있다.

```python
from time import sleep

def rest():
    print("쉬는시간 3초 전")
    sleep(3)
    print("쉬는시간이에용")

rest()
```

```
쉬는시간 3초 전
쉬는시간이에용
```

### non-blocking (JavaScript)

중간에 sleep이 들어가면 sleep에서 빠져나오기 전에 다음 코드를 실행한다.

```js
function rest() {
    console.log("쉬는 시간 3초 전")
    // setTimeout(<function>, <time:millisecond>)
    setTimeout(()=>{console.log("쉬는 시간 이에용")}, 3000)
    console.log("쉬는 시간 끝")
}

rest()
console.log("뭐지")
```

```
쉬는 시간 3초 전
쉬는 시간 끝
뭐지
쉬는 시간 이에용
```

> 하지만, 모든 자바스크립트의 함수가 non-blocking인것은 아니다.



### js에서 blocking sleep 만들기

```js
// javascript/day03/sleeptest2.js

function sleep(sec) {
    let start = Date.now()
    while (Date.now() < start + sec*1000) {}
}

function rest() {
    console.log("쉬는 시간 3초 전")
    sleep(3)
    console.log("쉬는 시간 이에용")
    console.log("쉬는 시간 끝")
}

rest()
console.log("원래대로 된다. 그런데 sleep이 끝날 때 까지 다른 동작을 할 수 없다 ㅠㅠ")
```

```
쉬는 시간 3초 전
쉬는 시간 이에용
쉬는 시간 끝
원래대로 된다. 그런데 sleep이 끝날 때 까지 다른 동작을 할 수 없다 ㅠㅠ
```



## Date.now()의 반환값의 정체

```js
Date.now()
// 1556080870620
```

1556080870620???



1556080870620은 1970년 1월 1일 0시 0분 0초 00을 기준으로 현재까지 몇 초가 흘렀는지 나오는 것으로

`협정 세계시(UTC)`에서 부터 흘러간 시간을 만하는 것이다.

이 기준을 `UNIX 기준시` 또는 `POSIX 시간`, `Epoch 시간`이라고 한다.
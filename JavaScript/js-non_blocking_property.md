# Non-blocking Property

js engine : multi thread

js : single thread

js가 단일 스레드로 동작하기 때문에 blocking 함수를 실행한 경우, js나 브라우저의 다른 기능을 사용할 수 없다.

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

> 현재 JavaScript 실력이라면 비동기적 = non-blocking property라고 알고 있으면 된다고 한다.
>
> 따라서 비동기적 = non-blocking property는 추후에 정리하겠습니다.

## 비동기적인 함수 활용하기

```js
const readFile = () => {
    let content
    // 파일을 읽어오는데 100ms 소요
    setTimeout(()=>{
        content = "Hello World"
    }, 100)
    return content
}

let fileContent = readFile()
console.log(fileContent)
// undefined
```

비동기적인 함수인 `setTimeout`을 사용하면 원하는 대로 동작을 처리할 수 없다.



```js
const readFile = (myFunc) => {
    let content
    // 파일을 읽어오는데 100ms 소요
    setTimeout(()=>{
        content = "Hello World"
        myFunc(content)
    }, 100)
    return content
}

const log = (content) => {
    console.log(content)
}

readFile(log)
// Hello World
```

따라서 `setTimeout`안에서 결과가 나온 뒤에 원하는 동작을 하기 위해서 `myFunc`를 인자로 받아서 `setTimeout`안에서 처리한다.



### FILE I/O를 통한 비동기 함수 활용

```js
// javascript/day04/test.md
This is a test file.
```

```js
// javascript/day04/callback.js
// FILE I/O
const fs = require('fs') // file system

// fs.readFile(<path>, <callback function>)
// callback function : (error, content) {console.log(error, content)}
fs.readFile(__dirname+'/test.md', 'utf8', (error, content) => {
    if (error === null) {
        console.log(content)
        // This is a test file.
    } else {
        console.log(error)
        // null
    }
})
```

- `fs` : `nodejs`에서 `file system`을 이용하기 위한 패키지
- `fs.readFile` : `utf8`인자로 인코딩으로 읽어서 `callback function`을 통해서  `path`에 있는 파일을 읽는 함수
- `__dirname` : 현재 파일이 위치하는 경로




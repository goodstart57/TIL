# JavaScript - convention

## define

### function

```js
// 함수 선언식
function sum1(a, b) {
    return a + b
}
```

```js
// 익명 함수를 변수에 저장
const sum2 = function (a, b) {
    return a + b
}
```

두 경우 중 두번째인 익명 함수를 변수에 저장하는 방법을 선호한다.

### string

문자열 정의할 때 `'`을 선호한다.



## call

### object value

```js
var profile = {
    first_name: "jaeseo",
    last_name: "lee",
    age: 27,
}

age = menus.age
first_name = menus["first_name"]
```

두 경우 중 `.`을 이용한 age 같은 방식을 선호한다.
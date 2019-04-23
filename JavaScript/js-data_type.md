# Start JavaScript

## 문법

### 상수 정의

```js
const name = "jaese"
name = "jaeseo"
```

```js
VM234:2 Uncaught TypeError: Assignment to constant variable.
	at <anonymous>:2:6
```



### 변수 정의

```js
let first_name = "jaese"
first_name = "jaeseo"
```



### for-loop

```js
for (var i = 0; i < 4; i++) {
    console.log(i)
}
console.log(i)
```

```js
0
1
2
3
4
```

for문 안에서 정의한 i가 loop을 다 돌고 나서도 `i++`을 한번 더 수행한 후에도 살아있다.

```js
for (let i = 0; i < 4; i++) {
    console.log(i)
}
console.log(i)
```

```
0
1
2
3
10
```

for문 안에서는 `let`으로 정의한 변수가 사용되고, for-loop 밖으로 나가서는 `var`로 정의한 i가 사용된다.

(첫번째 for-loop의 i와 두번째 i는 다른 스코프의 i)



### if

```js
let age = 22
if (age > 30) {
    console.log("30대 이상");
} else if (age > 20) {
    console.log("20대");
} else {
    console.log("10대 이하");
}
```



## DataType (자료형)

변수를 할당할 때 자료 자체를 저장하는 것이 아닌 자료의 주소값을 변수에 저장한다.

- 원시자료형 (Primitive)

  1. string

  2. number

  3. boolean

  4. null

     type edge case : `console.log(typeof(null))`을 사용하면 `object`가 나온다.

  5. undefined

  6. symbol

- 사용자 정의 자료형

  원시 자료형을 뺀 모든 자료형

  사용자 정의 자료형은 모든 것이 객체다.

  Object, Array, Function, Object (여기서 모든 것은 객체기 때문에 Object는 네번 반복된 것이다)

### Array + Array Helper Methods

```js
const names = ["john", "kcm", "ljs"]
```

#### Array.length

```js
names.length
// 3
```

#### Array.reverse

```js
names.reverse()
// (3) ["ljs", "kcm", "john"]
names
// (3) ["ljs", "kcm", "john"] : reverse 메소드는 원본이 바뀐다. (destructable)
```

#### Array.push

```js
names.push("jik")
// 4
names
// (4) ["ljs", "kcm", "john", "jik"]
```

#### Array.pop

```js
names.pop()
// "jik"
names
// (3) ["ljs", "kcm", "john"]
```

#### Array.shift

```js
names.shift()
// "ljs"
names
// (2) ["kcm", "john"]
```

#### Array.include

```js
names.includes("kcm")
// true
names.includes("k")
// false
```

#### Array.join

```js
names.join("와 ")
// kcm와 john
```

#### Array.forEach

```js
const posts = [
    {id: 1, title: "안녕"},
    {id: 2, title: "자바스크립트"},
    {id: 3, title: "브라우저 조작"}, // trailing comma
]

// forEach를 통해 순회를 하여 id가 2번인 post를 찾으세요
posts.forEach(post => {
    if (post.id === 2) {
        console.log(post);
    };
});
// {id: 2, title: "자바스크립트"}


/* 1. squaredNumbers를 numbers의 요소들을
 * 제곱을 한 숫자들의 배열로 만든다.
 * (for를 사용) */
let numbers = [0, 1, 2, 3, 4, 5, 6];
let squaredNumbers1 = [];

numbers.forEach(number => squaredNumbers1.push(number * number));
console.log(squaredNumbers1)
```

#### Array.map

```js
/* 2. map() */
let squaredNumbers2 = [];
squaredNumbers2 = numbers.map(number => number * number);
console.log(squaredNumbers2)
```





### Object

```js
const student = {'name': 'john', 'age': 20, 'isMale': true}
```

```js
const student = {name: 'john', age: 20, isMale: true}
```

student의 key에 `'` 를 붙이지 않아도 된다.

객체는 `mutable`

```js
student.name
// john
student['age']
// 20
```



### Function

```js
function helloWorld() {
    return "hello world" // return이 한줄 일 때 ;을 붙이지 않는다.
}
```

```js
const helloWorld = function() {
    return "hello world"
}
```

> JavaScript는 변수에 할당하는 방식을 더 선호한다.



### String

```js
var firstName = "JAESEO";
let introduction = `안녕하세요 저는 ${firstName}입니다`;
```

<code>`</code>을 사용하여 string interpolation을 사용할 수 있다.

```js
const me = {
	name: 'jaeseo',
	phone_number: '0123456789',
    products: {
        phone: 'iPhone 6s',
        notebook: 'LG Gram',
    }
}

console.log(me['name']);
// jaeseo
console.log(me.products['phone']);
// iPhone 6s
me.address = "종로구";
console.log(me);
// {name: "jaeseo", phone_number: "0123456789", products: {…}, address: "종로구"}
```

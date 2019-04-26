## Promise

비동기 로직이 끝나고 어떤 작업을 수행할 지 약속할 수 있다.

`Promise` 객체를 제어하기 위해서 `then`과 `catch` 메서드를 사용하는데 이 메서드의 리턴값도 `Promise`이다.

```js
const orderCoffee = (order) => new Promise((resolve, reject) => {
    /**
     * order가 제대로 들어왔는지 확인
     * 비동기적인 작업
     * resolve : 작업 성공 시
     * reject : 작업 실패 시
     */
    if (order === undefined) {
        // 실패
        reject('손님 주문해주시겠어요?')
    }

    let coffee
    setTimeout(() => {
        // 성공
        coffee = order
        resolve(coffee)
    }, 50)
});
```

`Promise`를 반환하여 카페에서 커피를 주문하는 함수 `orderCoffee` 정의



```js
orderCoffee('아아1')  // Promise ('아아'라는 값이 저장되어 있다.)
```

```
Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: "아아"

```



```js
orderCoffee('아아2')
    .then((coffee) => {
        console.log(coffee)
    })
```

```
아아

Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: undefined
```



```js
orderCoffee('아아3')
    .then((coffee) => {
        console.log(coffee+'(3-1)')
    })
    .then((coffee) => {
        console.log(coffee+'(3-2)')
    })
```

```
아아
undefined

Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: undefined
```



```js
orderCoffee()
    .then((coffee) => {
        console.log(coffee)
    })
    .catch((error) => {
        console.log(error+'1')
    })
```

```
손님 주문해주시겠어요?

Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: undefined
```



```js
orderCoffee()
    .then((coffee) => {
        console.log(coffee)
    })
    .catch((error) => {
        console.log(error+'2')
        return error
    })
```

```
손님 주문해주시겠어요?

Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: "손님 주문해주시겠어요?"
```



```js
orderCoffee('아아4')
    .then((coffee) => {
        console.log(coffee)
        return orderCoffee('라떼4')
    }) // Promise => 라떼
    .then((coffee) => {
        console.log(coffee) // 라떼
    })
    .catch((error) => {
        console.log(error+'3')
    })
```

```
아메리카노
라떼

Promise {<pending>}
    __proto__: Promise
    [[PromiseStatus]]: "resolved"
    [[PromiseValue]]: undefined
```



```js
fetch('https://koreanjson.com/posts/1')
    .then((response) => response.json()) // serialize => js object로 파싱
    .then((post) => console.log(post)) // 포스트 출력
    .catch((error) => console.log(error)) // 예외처리
```




## async - await

```js
const getCoffee = async (order) => {
    const coffee = await orderCoffee(order)
    console.log(coffee)

    const coffee2 = await orderCoffee('아아')
    console.log(coffee2)
}

getCoffee('따아')
```

- `async` : 함수 정의하는 구문 앞
- `await` : 비동기 적으로 작동하고 싶은 동작 앞
- 두가지 함수를 이용하여 정의하는 함수를 동기적으로 동작하도록 정의



### fetch 함수를 async-await으로 구현하기

```js
const URL = 'https://koreanjson.com/posts/1'
```

#### fetch

```js
fetch(URL)
    .then((response) => response.json())
    .then((post) => console.log(post))
    .catch((error) => console.log(error))
```

```
Promise {<pending>}

VM145:3 {id: 1, title: "정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.", content: "모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 모든 국민은…진다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다.", createdAt: "2019-02-24T16:17:47.000Z", updatedAt: "2019-02-24T16:17:47.000Z", …}

VM145:1 Fetch finished loading: GET "https://koreanjson.com/posts/1".
```



#### async-await

```js
const getPosts = async (URL) => {
    const response = await fetch(URL)
    console.log(response)

    const post = await response.json()
    console.log(post)
}

getPosts(URL)
```

```
Promise {<pending>}

VM140:3 Response {type: "cors", url: "https://koreanjson.com/posts/1", redirected: false, status: 200, ok: true, …}

VM140:2 Fetch finished loading: GET "https://koreanjson.com/posts/1".

getPosts @ VM140:2
(anonymous) @ VM148:1
VM140:6 {id: 1, title: "정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.", content: "모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 모든 국민은…진다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다.", createdAt: "2019-02-24T16:17:47.000Z", updatedAt: "2019-02-24T16:17:47.000Z", …}
```


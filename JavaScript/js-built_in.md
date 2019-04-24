# built-in Objects

## Functions

### typeof(object/variable)

객체/변수의 데이터 타입을 반환

```js
console.log(typeof(1))
// number
console.log(null)
// object
console.log(undefined)
// undefined
```



## JSON Object

javascript object의 형태와 유사하게 생긴 file으로 하나의 문자열이다.

#### JSON.parse(json)

json stringto js object

| #      | input/output | description       |
| ------ | ------------ | ----------------- |
| args   | json         | json string       |
| return | object       | javascript object |

#### JSON.stringify(object)

js object to json string

| #      | input/output | description       |
| ------ | ------------ | ----------------- |
| args   | object       | javascript object |
| return | json         | json string       |


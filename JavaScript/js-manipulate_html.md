# JS로 HTML 조작하기

`document` 사용



## write

```js
document.write("HTML 문서")
```

```js
document.write("<h1>아무말</h1>")
document.write("<p>JS에서 HTML 사용하기</p>")
```



## querySelector

```js
document.querySelector('태그의 이름')
```

```js
document.querySelector('p')
```



## querySelector를 이용하여 HTML 조작하기

```js
ptag = document.querySelector('p')
ptag.innerText = "JS에서 HTML문서 조작하기"
```



### 
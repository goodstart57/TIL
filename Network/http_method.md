# HTTP Method

## GET

정보를 가져오다.

거의 모든 서비스에서 기본 값으로 사용된다.

```python
import requests

url = 'http://www.naver.com'
response = requests.get(url)
response
```

```
<Response [200]>
```

http request 방식 중 간단한 식으로 데이터를 전송할 때에도 ?data=you&want=totransfer 와 같이 url 상에서 데이터를 전송할 수 있다.

## POST

게시물을 올리다. 데이터를 전송하다.

```python
import requests

url = '<some your api url>'
contents = {'data': 'you', 'want': 'to', 'transfer':'.'}
response = requests.get(url, contents)
response
```

```
<Response [200]>
```

포스트 방식의 경우, 데이터를 api를 통해 보낼수 있으면 get 방식과 달리 url에 데이터가 포함되지 않기 때문에 get 방식보다 비교적 안전하다.



이상으로 HTML4시대에 나온 방법이다.

이러한 방식으로 URL(Uniform Resource Locator)을 사용하게 되는데

자원이라는 의미의 URL에 동사가 들어가는것을 막기 위해서

HTML5부터 PATCH/DELETE 요청 방법이 나온다.

```
HTML4 => HTML5

getarticles/1/retrievecomments => articles/1/comments (GET)

getarticles/1/deletecomments => articles/1/comments (DELETE)
```



위와 같이 URL이 깔끔해졌다.




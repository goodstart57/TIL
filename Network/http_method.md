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
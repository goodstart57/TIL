# How to debug in Django

주피터 같은 곳에서 장고환경을 불러올 수 없기 때문에 쉘에서만 디버깅하기 어렵다.

하지만 `IPython`패키지를 이용하면 `views.py`의 `request`안에 무엇이 들어있는지 알 수 있다.

```python
# app/views.py
from django.shortcuts import render
from board.models import Article, Comment
from IPython import embed

def article_list(reqeust):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    embed()
    return render(reqeust, 'board/list.html', context)
```

위와 같이  `views.py`를 생성하여 웹페이지를 불러오면 runserver를 실행하고 있는 터미널에서 IPython이 플로팅되어 디버깅이 가능하다.

IPython을 통하여 reqeust를 확인해보면 다음과 같이 볼 수 있다.



```
In [2]: reqeust
Out[2]: <WSGIRequest: GET '/board/'>
In [4]: type(reqeust)
Out[4]: django.core.handlers.wsgi.WSGIRequest
```


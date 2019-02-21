# Database 관계

## 관계

두 엔티티 사이의 논리적인 관계를 말한다.

## 관계 차수

### 1:1

one to one

사람과 주민등록번호

현실에서는 잘 쓰이지 않는다.

### 1:N

one to many

학급과 학생

### M:N

Many to many

수강신청 (수업, 학생)

### 관계 없음



## Example on Django ORM

### 1:N

```python
# articles/models.py
from django.db import models

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

`Article : Comment = 1 : N`라는 것을 Comment 모델의 article 컬럼으로 표현한다.

이때 `models.ForeignKey`를 사용하며 인자로는 `대상이 되는 모델`과 `on_delete`를 설정해주어야 한다.

#### on_delete

- CASCADE

  Foreign Key로 관계된 객체가 삭제면 관련된 모든 객체가 삭제

- PROTECT

  Foreign Key로 관계된 객체가 삭제되려고 할 때 [`ProtectedError`](https://docs.djangoproject.com/ko/2.1/ref/exceptions/#django.db.models.ProtectedError)를 일으킴

- SET_NULL

  `Foreign Key`에 `NULL`을 지정하기 위해서 `null=True` 인자와 함께 설정

- SET_DEFAULT

  `Foreign Key`에 `default` 값을 설정합니다. 따라서 `default` 인자도 설정
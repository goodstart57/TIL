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

Many to many, 수강신청 (수업, 학생)

RDBMS에서 M:N 관계를 표현할 수 없기 때문에 `pivot table`을 생성해서 간접적으로 표현한다.

Django에서 models.ManyToManyField를 이용하여 구현할 수 있으며 두 모델(테이블) 중 한 곳에만 쓰면 된다.

```python
"""숙소 예약"""
class Client(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ('name', )


class Resort(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client)
```

```sqlite
--
-- Create model Client
--
CREATE TABLE "sugangs_client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL);
--
-- Create model Resort
--
CREATE TABLE "sugangs_resort" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(30) NOT NULL
);
CREATE TABLE "sugangs_resort_clients" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "resort_id" integer NOT NULL REFERENCES
    "sugangs_resort" ("id") DEFERRABLE INITIALLY DEFERRED,
    "client_id" integer NOT NULL REFERENCES
    "sugangs_client" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE UNIQUE INDEX "sugangs_resort_clients_resort_id_client_id_12b12781_uniq" ON "sugangs_resort_clients" ("resort_id", "client_id");
CREATE INDEX "sugangs_resort_clients_resort_id_7b3321d2" ON "sugangs_resort_clients" ("resort_id");
CREATE INDEX "sugangs_resort_clients_client_id_13c6c569" ON "sugangs_resort_clients" ("client_id");
COMMIT;
```



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







```python
class Project(models.Model):
    # Relations
    user = models.ForeignKey(
        Profile,
        related_name="projects",
        verbose_name=_("user")
        )
    # Attributes - Mandatory
    name = models.CharField(
        max_length=100,
        verbose_name=_("name"),
        help_text=_("Enter the project name")
        )
    color = models.CharField(
        max_length=7,
        default="#fff",
        validators=[RegexValidator(
            "(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)")],
        verbose_name=_("color"),
        help_text=_("Enter the hex color code, like #ccc or #cccccc")
        )
    # Attributes - Optional
    # Object Manager
    objects = managers.ProjectManager()
    # Custom Properties
    # Methods
 
    # Meta and String
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ("user", "name")
        unique_together = ("user", "name")
 
    def __str__(self):
        return "%s - %s" % (self.user, self.name)
```


# ORM

**Object-relational mapping**



## ORM의 장점

1. reuse

MySQL, Oracle SQL, PostgreSQL, Sqlite3 등등 수많은 Database가 있고, 각각 약간의 차이가 있다.

Sqlite3를 쓰다가 추후에 MySQL로 바꾸게 된다고 했을때 ORM을 이용한다면 sql 코드 자체를 바꿀 필요가 없다.

ex) 배달의 민족

2. user-friendly

`Article.query.all()`을 봤을때 개발자가 아닌 분이라도 모든(all()) 기사를(Article) 조회(query)해라는 것을 알 수 있을 정도로 인간에게 친숙한 언어이다.



## ORM in Flask

### Install flask ORM package

```bash
$ sudo pip3 install sqlalchemy
$ sudo pip3 install flask-sqlalchemy
```



### Init flask ORM

```python
# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog2.db"  # db name
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
db.init_app(app)
```

기존 flask 프로젝트를 생성하는 것과 같이 `app.py`에 app 인스턴스를 생성합니다.

이 프로젝트에 SQLALCHEMY를 이용하기 위해서 config를 설정합니다.

`SQLAlchemy` 인스턴스 `db`를 생성합니다.

이것으로 flask에서 ORM을 사용할 준비가 끝났습니다.



### Create Table Article

```sqlite
-- create articles table in sqlite3
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
);
```

```python
# app.py
# create article table in orm
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

db.create_all()
```



### Create (Insert Record)

```sqlite
-- insert record in sqlite3
INSERT INTO articles (title, content) VALUES ('hi', 'im jaeseo');
```

```python
# insert record in orm
db.session.add(Article(
    title="hi",
    content="im jaeseo"
))
db.session.commit()
```



### Read

```sqlite
-- read record in sqlite3
SELECT * FROM articles WHERE id = 28;
```

```python
# read record in sqlite3
Article.session.get(28)
```



```sqlite
-- read record in sqlite3
SELECT * FROM articles WHERE title = 'hi';
```

```python
# read record in sqlite3
Article.session.filter_by(title="hi")
```


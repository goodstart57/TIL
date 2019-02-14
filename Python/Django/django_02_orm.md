# ORM in Django

## Table Info

```python
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"제목: {self.title}, 내용: {self.content}"
    
    def __str__(self):
        return f"제목: {self.title}, 내용: {self.content}"
```



## Python Console in Django Config

```bash
$ ls
articles/  db.sqlite3  manage.py*  pracdb/
$ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 02:16:34) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Here you can test django orm!
```



## ORM

### Load Article model (table)

```python
from articles.models import Article
```

### Create

```python
Article(title="hello", content="this is JAESEOLEE").save()
a = Article(title="hello", content="this is JAESEO")
a.save()
```

```
No Return Value or Text
```

### Read

```python
my_article = Article.objects.get(title="hello", content="this is JAESEO")
print(my_article)
```

```
제목: hello, 내용: this is JAESEO
```

```python
my_articles = Article.objects.filter(title="hello")
print(my_article)
```



### Update

```python
my_article = Article.objects.filter(title="hello").first()
my_article.title = "hi"
my_article.save()
```


### Delete

```python
my_article = Article.objects.filter(title="hi")
my_article.delete()
```


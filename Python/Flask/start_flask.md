# Flask

OS : Ubuntu 14.04.5 LTS

Cloud9 (not aws cloud9)

Latest : 1.0.2

[http://flask.pocoo.org/](http://flask.pocoo.org/)

## Install flask package

```
sudo pip3 install flask
```

## Start Flask

__URL__

Before starting flask project,

To explore url configuration, I take an example for https://search.naver.com/search.naver?query=flask

This url can search `flask` on naver.

`https://` : protocol

`search.naver.com` : Domain of naver search

`search.naver` : Request to search

`query=flask` : search flask

__Start flask project on `flask` directory__

```python
# flask/app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

__setup easy on cmd__

```
$ pip install Flask
$ FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080
 * Running on https://<project.name>-<user.name>.c9users.io:8080
```

My project.name is `flask` and user.name is goodstart, so we can access my index page on cloud9 flask server  by `https://flask-goodstart.c9users.io/`

You can access your index page existing "Hello World" String.

__variable routing__

add function to say hello and name input

```python
# app.py
from flask import Flask

app = Flask(__name__)
    
@app.route("/hello/<name>")
def hi(name):
    return "hello {name}".format(name=name)
```

We can use the input value in the route argument. (name)



## Really Start to make Flask Project

I would to create Flask Project can search Google, Naver and Daum

Firstly, import Flask class and make Flask instance.

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)
```



and then, you should make index page and app function



```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Fake Search</h1>
    <h2>Google Search</h2>
    <form action="https://www.google.com/search">
        <input type="text" name="q">
        <input type="submit">
    </form>
    <h2>Naver Search</h2>
    <form action="http://search.naver.com/search.naver">
        <input type="text" name="query">
        <input type="submit">
    </form>
    <h2>Daum Search</h2>
    <form action="https://search.daum.net/search?w=tot&">
        <input type="text" name="q">
        <input type="submit">
    </form>
</body>
</html>
```



At once, you can search google, naver and daum search on your index page, like below



![index page can search a variety of search site](..\images\flask_index_search_page.JPG)
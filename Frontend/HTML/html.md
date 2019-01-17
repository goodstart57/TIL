# Basic HTML (HyperText Markup Language)

You can move other HTML documents and construct web page by using HTML tags.

`Hyper` means that we can move around HTML documents

## basic template

```html
<!DOCTYPE html>
<html>
    <head>
        <!-- head : information about this document -->
        <title>Test HTML</title>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- body : important context -->
        <h1>Test HTML</h1>
        <!-- most important context -->
        <h2>Sub Title</h2>
        Hello
    </body>
</html>
```

html use <!-- --> comment

```
HTML must follow Web Standards

for example, h1 should be used only once.

If not, your homepage is not searched from google.
```

[web standards](https://www.w3.org/standards/)

<br>



__in vs code__

input ! and push tab then html basic construction is printed like below code.

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
    
</body>
</html>
```





## HTML tags

there are various tags to construct web page in HTML

### a

`a` (anchor) tag can link other HTML document, media and so on!


```html
<!-- example -->

<a href="https://www.naver.com">link to naver</a>
```



write link to move other HTML in href



### header

\<h1\> ~ \<h6\> is title tag

The letter size decreases from \<h1\> to \<h6\> 



### img 

`img` tag can load image

```html
<!-- example -->

<img width="560" src="https://dobsondev.com/wp-content/uploads/2017/05/css-featured-image.jpg" alt="html logo">
```



write local path or url to load image



### iframe

`iframe` tag can load video

```html
<!-- example -->

<iframe width="560" height="315" src="https://www.youtube.com/embed/Tt3kr7whkb4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```



![youtube share button](../images/youtube-share.png)

You can copy iframe tag from share of youtube video 



### form 

you can access web page, file, when you input the enter on input tag



### input

User can input string in the `input` tag.

With form tag, you can access web page, file you want

```html
<form action="https://www.google.com/search">
    <input type="text" name="q">
    <input type="submit">
</form>
```

If you just write "/search" without domain, then access to your domain + form action  + input tag + text you typed





### table

```html
<table>
    <tr>
    	<td>나이</td>
        <td>575살</td>
    </tr>
    <tr>
      <td>대학교</td>
      <td>조선도적사관학교</td>
    </tr>
    <tr>
      <td>혈액형</td>
      <td>O형</td>
    </tr>
</table>
```



list

ol (ordered list), ul(unordered list)

```html
<ol>
    <li>1</li>
    <li>2</li>
    <li>3</li>
</ol>
<ul>
    <li>3</li>
    <li>2</li>
    <li>7</li>
</ul>
```









## Attribute of HTML 

### ID and Class

id is unique, but class is not unique

so class is used to grouping each elements

```html
<!-- div example -->

<div id="title" class="introduce">This is JAESEO LEE</div>
```

We can find multiple tags by searching class, and specific word by searching id



<br>



```
HTML is important skeleton, however, it isn't pretty.

If you want to decorate HTML document, then css can help you!

+ when you meet js and python (or ruby, nodejs etc..), feel wonderous
```



## Tip

### shorcut making tag

if you want to cereate `<div class="my"><div></div></div>`

just write `div.my>div`
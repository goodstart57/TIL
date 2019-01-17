<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

# SaaS (Software as a Service)

서비스로서의 소프트웨어

서비스는 요청과 응답으로 이루어 진다.

Web Service?

WWW는 정보 공간을 의미하고 간단하게 web과 동의어다.

## ip, domain

IP

Domain

## Web

### Static Web

### Dynamic Web(Web APP / Web Application)

사용자의 요청에 따라 서비스를 제공하는 웹

## URL

> http(s)://hphk/lectures/1

위와 같이 url을 명시적으로 표시하는 것이 restful한 것에 중요



## HTML

### Head



### Body

브라우저 화면에 나타나는 정보로 실제 내용에 해당된다.



### tag

#### self-closing element

```html
<img src="url"/>
```

위와 같이 self-closing element는 마지막 꺽쇠 전에 "/"를 넣는것을 권장한다.

#### 시맨틱태그


유저들은 새로운 ui를 겪는데 스트레스를 받기 때문에 웹페이지들의 표준을 정해서 유사하게 제작한다.

- \<header\>
- \<body\>
- \<aside\>
- \<footer\>



## CSS

### HTML과 CSS의 연결

#### inline tag

```html
<span style="color:blue;">This is my site</span>
```

#### style tag

```css
<style>
    span {
        color: blue;
    }
</style>
```

#### import css file


### Selector

### Bootstrap

class를 기반으로 css를 조정할 수 있다.

##### .display-1, .display-2, .display-3, ...

##### .m-0

margin: 0;

##### .mt-0

margin-top: 0;

##### .ml-0

margin-left: 0;

##### .mx-0

margin-left: 0;

margin-right: 0;

##### .mt-1

margin-top: 4px;

##### .mt-n

margin-top: 2^(n+1)px;

##### 정리하면

m : margin

p : padding

t : top

b : bottom

l : left

r : right

x : left, right

y : top, bottom

0 : 0 : 0px

1 : 0.25 : 4px

2 : 1 : 8px

... : ... : ...

5 : 2.5 : 64px

##### 음수도 가능

.my-n0

n0 : 0 : 0px

n1 : -0.25 : -4px

... : ... : ...

n5 : -2.5 : -64px



#### Color

감각적인 색상으로 바꿔준다.

##### primary

##### secondary

##### success

##### info

##### warning

##### danger

##### light

##### dark

혼자 사용되는것이 아닌 bg-primary, text-success와 같이 특정 영역에 사용된다.



#### border

##### border

##### border-success

##### rounded



#### grid

콘텐츠간의 비율 특히 가로 배치가 중요하다.

12격자 - 약수가 많은 수
# TMUX 그리고 단축키

가끔씩 사용하는데 사용할 때마다 찾아보려니 여간 번거로운것이 아니다.

내친김에 정리하기로 한다.



## TMUX란?

([위키주의](<https://ko.wikipedia.org/wiki/Tmux>)) **tmux**는 사용자가 단일 단말기 창 또는 원격 터미널 세션 안에서 여러 별도의 터미널 세션에 액세스할 수 있도록 여러 가상 콘솔을 다중화하는데 사용할 수 있는 응용 소프트웨어이다. 이 응용 프로그램은 명령어 인터페이스로부터 다수의 프로그램을 처리하고 [유닉스 셸](https://ko.wikipedia.org/wiki/유닉스_셸)로부터 프로그램을 분리하는 데에 유용하다.[[2\]](https://ko.wikipedia.org/wiki/Tmux#cite_note-openbsd-faq-2) 이것은 [GNU Screen](https://ko.wikipedia.org/wiki/GNU_Screen)과 동일한 기능을 많이 제공하지만 [BSD 허가서](https://ko.wikipedia.org/wiki/BSD_허가서)로 배포된다....

🤔 리눅스에서 여러 터미널창을 켜고 작업하기 편하도록 만든 프로그램인 것 같다.

🤔 다수의 프로그램을 처리하고 유닉스 셸로부터 프로그램을 분리 ==> tmux의 세션작업하는 경우 내 작업이 의문사하는 경우를 줄여주는 좋은 기능을 가지고 있다.



### TMUX 용어

#### 세션(Session)

TMUX에서 가장 큰 단위로 여러개의 윈도우를 관리할 수 있다.

#### 윈도우(Window)

크롬 브라우저의 탭처럼 한 세션(브라우저)에서 여러 윈도우(탭)을 가질 수 있다.

대개 하나의 윈도우만 사용한다.

\+ 여러 세션에 속할 수 있다.

#### 페인(Pane)

한 윈도우를 pane border으로 쪼개어 여러 작업을 할 수 있도록 도와준다.

크기나 위치를 조절 할 수 있기 때문에 tmux의 강력한 기능이다.



~~다쓰고나니 용어명이 전부영어구나~~



## TMUX 명령어 & 단축키

### 쉘 명령어

#### 세션 생성

```shell
tmux new
tmux new -s <session_name>
```

새로운 세션을 생성한다.

세션명을 지정하지 않으면 세션명이 번호로 생성된다



#### 세션 종료

```shell
(session 안에서) exit
ctrl + d
ctrl + b + d
```

1, 2의 경우 세션이 kill 되면서 나오며, 3의 경우 세션이 살아있는 채로 빠져나온다.



#### 세션 리스트 보기

```shell
tmux ls
```



#### 세션 재접속

```shell
tmux attach -t <session_name or session_number>
```




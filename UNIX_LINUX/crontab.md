# crontab (크론탭)

linux 스케줄러 프로그램



## 기본 사용법

### crontab -e

스케줄러 설정

최초 실행 시 에디터 설정 후 설정 화면으로 넘어간다.

```bash
$ crontab -e
no crontab for ubuntu - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 2
No modification made
```



### crontab -l

현재 설정되어있는 스케줄러 리스트 출력





## 스케줄러 등록

`crontab -e` 으로 스케줄러 등록 화면으로 이동 가능하다.

```bash

# 매분 my_program.sh 실행
# [분(0-59)] [시간(0-23)] [일(1-31)] [월(1-12)] [요일(0-7)] [command]
* * * * * sh my_program.sh


# 매월 1일 00:00에 my_program.sh 실행
0 0 1 * * sh my_program.sh
```


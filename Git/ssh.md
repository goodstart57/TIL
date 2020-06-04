# Github SSH 연결하기 (Git 비밀번호 없이 사용하기)

## 1. public key 만들기
```cmd
$ cd ~/.ssh
$ ssh-keygen
Generating puglic/private rsa key pair.
Enter file in which to save the key (/home/username//.ssh/id_rsa):
```
key가 생성될 디렉토리 입력 (엔터로 넘어가면 현재 위치에 생성)

```cmd
Enterpassphrase (empty for no passphrase) :
Enter same passphrase again:
```
비밀번호 입력 (엔터로 넘어가면 다음에 안물어본다)

동일하게 진행했다면 `~/.ssh/id_rsa.pub` 생성

`cat ~/.ssh/id_rsa.pub` 출력된 내용을 복사 (ssh-rsa 부터 복사)

## 2. Github에 등록

우측 상단 프로필 > Settings > SSH and GPG keys > New SSH key 클릭

원하는 `Title` 입력

public key를 `key`에 복사 (ssh-rsa 부터 입력)

-끝-





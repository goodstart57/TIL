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


## 3. 다시 Clone하기

ssh 연결을 적용하기 위해서 

`Clone을 원하는 Repository Page` 접속 > `Clone or download` 클릭 > `Clone with SSH` > url으로 원하는 경로에 clone

```cmd
jfrost@ip-172-31-20-18:/home/jfrost/Workspace$ git clone git@github.com:goodstart57/TIL.git
Cloning into 'TIL'...
The authenticity of host 'github.com (52.78.231.108)' can't be established.
RSA key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,52.78.231.108' (RSA) to the list of known hosts.
remote: Enumerating objects: 166, done.
remote: Counting objects: 100% (166/166), done.
remote: Compressing objects: 100% (116/116), done.
remote: Total 557 (delta 43), reused 139 (delta 27), pack-reused 391
Receiving objects: 100% (557/557), 2.71 MiB | 2.31 MiB/s, done.
Resolving deltas: 100% (183/183), done.
jfrost@ip-172-31-20-18:/home/jfrost/Workspace$ gs
fatal: not a git repository (or any of the parent directories): .git
```

-끝-
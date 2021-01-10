# Github SSH 연결하기 (Git 비밀번호 없이 사용하기)

windows에서는 자동으로 비밀번호가 등록되어 id/pw 입력 없이 git bash에서 사용할 수 있지만,

linux에서는 일일히 입력하기 여간 귀찮은 부분이 아니다.

ssh 연결으로 조금이라도 편하게 git commit/push 해보자.



## 1. public key 만들기
```cmd
$ cd ~/.ssh
$ ssh-keygen
Generating puglic/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
```
key가 생성될 디렉토리 입력 (엔터로 넘어가면 위에서 물어보는 위치에 생성)

```cmd
Enterpassphrase (empty for no passphrase) :
Enter same passphrase again:
```
비밀번호 입력

여기까지 진행했다면 `~/.ssh/id_rsa.pub` 으로 public key가 생성되었다.

`cat ~/.ssh/id_rsa.pub` 출력된 내용을 복사 (처음부터 끝까지 복사)




## 2. Github에 등록

우측 상단 프로필 > Settings > SSH and GPG keys > New SSH key 클릭

원하는 `Title` 입력

public key를 `key`에 복사 (처음부터 끝까지 입력)



## 3. 내 repositroy 연동방식 변경

### remote url 변경

ssh 연결을 적용하기 위해서 다시 clone할 수도 있지만 이는 git에서 쓰는 `origin`라는 변수에 저장된 주소를 변경하기 위함이다.

```bash
local:~/Workspace$ git remote set-url origin git@github.com:[github계정명]/[repository명].git
```

위 명령어를 실행하면 origin에 저장된 repository 주소가 `https에서 ssh방식`으로 변경 적용된다. 

- ssh버전의 주소는 내 `github repository page >  Code > ssh`에서 url을 복사하면 된다.



### 그냥 clone하기

remote고 뭐고 복잡해서 싫다? 그냥 clone을 다시하면 된다.

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
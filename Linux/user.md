# LINUX User Management(리눅스 계정관리)

권한 관리를 위한 리눅스 계정 관리

```bash
# 사용 os
ubuntu@ip-172-31-31-248:~/mng$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
```

[ref : conory [기본] 리눅스의 사용자 계정 관리하기](https://conory.com/blog/12797)



## 계정 관리

### 계정 목록

```bash
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin

# [계정ID] : [계정의 패스워드 유무] : [UID] : [GID] : [사용자 설명] : [사용자 홈디렉토리] : [쉘]
```

- 계정ID : 이 계정 ID를 이용해 계정에 접속할 수 있지요.. 계정의 이름입니다.
- 계정의 패스워드 : 원래는 여기에 패스워드가 기록되어있는 데 보안상 문제로 인해 현재는 패스워드 존재여부만 나타냅니다. (x는 있음)
- UID : 시스템상에서 사용되는 사용자계정의 고유 식별번호입니다. 겹치면 심각한 오류가 납니다.100번까지는 시스템이 사용합니다..
- GID : 시스템상에서 사용되는 사용자그룹의 고유 식별번호입니다.  499번까지는 시스템이 사용합니다.. 그룹에 대해 나중에 설명하겠습니다.

- 사용자 설명 : 해당 계정에 대해 설명을 적습니다. 없다면 비워두셔도 됩니다.

- 사용자 홈디렉토리 : 사용자의 개인폴더입니다. 계정에 로그인시 이 경로로 이동됩니다. 기본은 "/home/계정ID"로 지정됩니다.

- 쉘 : 사용자 로그인시 사용되는 쉘입니다. 기본으로 /bin/bash (Bourne Again Shell) 이 지정됩니다.



### 계정 추가

```bash
$ sudo adduser jfrost
Adding user `jfrost' ...
Adding new group `jfrost' (1001) ...
Adding new user `jfrost' (1001) with group `jfrost' ...
Creating home directory `/home/jfrost' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for jfrost
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] Y
```

계정과 함께 home directory 가 정상적으로 생성된 모습이다.



```bash
# useradd [option] [username]
$ sudo useradd testusr
```

정상적으로 계정이 생성되면 아무것도 출력되지 않는다.

```bash
$ sudo cat /etc/passwd | grep testusr
testusr:x:1002:1002::/home/testusr:/bin/sh
```

계정이 잘 생성되었는지 확인...

하지만 `/home/testusr`가 존재하지 않는다!



😂 위 방법대로 `useradd` 명령어로 계정을 생성하면 home directory가 생성되지 않아서 su로 유저 변경을 하던 접속을하던 에러가 난다. 꼭 `-m` option을 붙여서 `sudo useradd -m testusr`와 같이 유저 생성할것. 

```bash
$ sudo useradd -m testusr
$ ll /home
total 20
drwxr-xr-x  5 root    root    4096 Jan 10 14:54 ./
drwxr-xr-x 19 root    root    4096 Jan  9 16:25 ../
drwxr-xr-x  2 chicken chicken 4096 Jan 10 14:54 testusr/
drwxr-xr-x  2 jfrost  jfrost  4096 Jan 10 14:53 jfrost/
drwxr-xr-x  6 ubuntu  ubuntu  4096 Jan 10 14:47 ubuntu/
```



### 계정에 비밀번호 부여

```bash
# passwd [option] [username]
$ sudo passwd jfrost
New password:
Retype new password:
passwd: password updated successfully
```

[option]

- -d : 계정에 부여된 패스워드를 삭제합니다.
- -l : 패스워드를 잠급니다. (잠그면 사용자가 계정에 접속하지못합니다.)
- -u : 패스워드 잠금을 해제합니다.
- -S : 현재 패스워드 상태를 출력합니다.

[username]

- 패스워드를 부여하고 싶은 계정ID를 입력합니다.







[ref : conory [기본] 리눅스의 사용자 계정 관리하기](https://conory.com/blog/12797)
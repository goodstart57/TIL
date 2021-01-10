# SSH (Secure SHell)

네트워크 보안 도구 중 하나로 원격접속을 안전하게 할 수 있게 해주는 프로토콜이다.

AWS ec2로 만들어진 리눅스 서버를 이용할 때 ssh로 서버접속을 흔히들 사용한다.

| 사용 OS | Version                   |
| ------- | ------------------------- |
| Ubuntu  | 20.04.1 LTS (Focal Fossa) |



## SSH란

1995년 핀란드의 타투 일료넨(Tatu Ylönen)이 설립한 시큐어 셸 커뮤니케이션 시큐리티(SSH Communication Security)사에 의해 개발 및 상용화되었다.

인터넷상에서 두 호스트(Host) 사이의 통신 암호화 관련 인증 기술들을 사용하여, 안전한 접속과 통신을 제공하는 [프로토콜](https://terms.naver.com/entry.nhn?docId=1167759&ref=y)을 의미한다. 이 프로토콜은 보안에 취약점을 가지고 있는 프로토콜, 즉 원격 로그인(rlogin), 원격 명령 실행(rsh), 원격 파일 복사(rcp), 원격 접속 서비스(telnet), 파일 전송용 프로토콜(ftp) 등을 대체하여 사용되며, 임의의 포트에 대해 안전한 채널을 제공하고 있다.

원격 접속에서 가장 중요한 부분이 인증 방법인데, 기본적으로는 사전에 미리 약속된 공개키를 사용하여 전자 서명을 통해 인증을 하지만, 공개키를 사용한 전자 서명에 의한 인증이나 다른 인증 방법들이 사용될 수 없는 경우에는 전통적인 인증 방식인 패스워드를 사용하여 인증을 하게 된다. 이러한 경우에도 호스트 사이의 모든 통신이 암호화에 의해서 자동 보호되기 때문에 어떠한 네트워크 공격으로도 패스워드가 노출되지 않는다.

보안 솔루션을 갖추지 않은 조직이나 개인이 안전한 원격 접속 작업을 할 수 있는 간편한 솔루션이 제공되며, 주요 소프트웨어 회사들도 관련 제품을 개발하고 있다. 상용화된 이후 SSH 1.2.12를 기반으로 하여 [오픈소스](https://terms.naver.com/entry.nhn?docId=1228317&ref=y)로 작성된 OpenSSH 프로젝트가 시작되었으며, OpenSSH 7.1 버전까지 개발되었다.

**[네이버 지식백과]** [시큐어 셸](https://terms.naver.com/entry.nhn?docId=3351634) [Secure Shell] (두산백과)

---



## SSH 접속 방법

```bash
# ssh [username]@[ip] -i [secure key]
local:~ $ ssh ubuntu@ec2-어쩌구-저쩌구-ip-주소.ap-northest-2.compute.amazonaws.com -i mysecure.pem
```

ssh key 생성 관해서는 시도1에서 볼 수 있다.

ec2의 경우는 기본적으로 private key file을 제공한다.



## 다른 계정에 SSH 접속하면? Permission denied (publickey).

"chicken"이라는 계정을 ubuntu 서버에 추가한 뒤에 로컬에서 ssh 접속을 시도해봅니다.

```bash
ubuntu@server:~ $ sudo adduser chicken
ubuntu@server:~ $ exit
```

```bash
local:~ $ ssh chicken@ec2-어쩌구-저쩌구-ip-주소.ap-northest-2.compute.amazonaws.com -i mysecure.pem 
chicken@ec2-어쩌구-저쩌구-ip-주소.ap-northeast-2.compute.amazonaws.com: Permission denied (publickey).
```



### 시도1: chicken 계정에 private key를 추가하여 시도해본다. 

```bash
chicken@server:~ $ ll ~
total 20
drwxr-xr-x 2 chicken chicken 4096 Jan 10 15:37 ./
drwxr-xr-x 5 root    root    4096 Jan 10 15:37 ../
-rw-r--r-- 1 chicken chicken  220 Jan 10 15:37 .bash_logout
-rw-r--r-- 1 chicken chicken 3771 Jan 10 15:37 .bashrc
-rw-r--r-- 1 chicken chicken  807 Jan 10 15:37 .profile
```

새로 생성된 계정이라서 .ssh 경로에 key 파일이 없습니다.

```bash
chicken@server:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/chicken/.ssh/id_rsa): [파일 만들 경로 (default가 왼쪽 경로)]
Created directory '/home/chicken/.ssh'.
Enter passphrase (empty for no passphrase): [내 비밀번호]
Enter same passphrase again: [내 비밀번호 재입력]
Your identification has been saved in /home/chicken/.ssh/id_rsa
Your public key has been saved in /home/chicken/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:OVC5imOL5DDNnYs96HsSQRJHj88KineHvEsY8XsAtSk chicken@ip-172-31-31-248
The key's randomart image is:
+---[RSA 0000]----+
| 그    으   림    |
+----[SHA256]-----+
```

`ssh-keygen`으로 현재 경로에 내 비밀번호 값을 가진 key 파일을 생성하여 보안키를 로컬에 저장. (chicken-access.pem)

- ~/.ssh/id_rsa : 보안키 (client에서 가지며 공개키와 대조하여 일치하는지 확인한다.)
- ~/.ssh/id_rsa.pub : 공개키 (server에서 가지고 있는다.)

```bash
local:~ $ sudo chmod 0400 chicken-access.pem
local:~ $ ssh ubuntu@ec2-어쩌구-저쩌구-ip-주소.ap-northest-2.compute.amazonaws.com -i chicken-access.pem
Are you sure you want to continue connecting (yes/no)? yes
Enter passphrase for key 'chicken-access.pem':
chicken@ec2-어쩌구-저쩌구-ip-주소.ap-northeast-2.compute.amazonaws.com: Permission denied (publickey).
```

접속을 시도했으나 알수없는 이유로 접속이 막혔다.



### 시도2: sshd 설정 변경

```bash
ubuntu@server:~$ sudo vim /etc/ssh/sshd_config
ubuntu@server:~$ sudo sshd restart
```

sshd(ssh 접속을 도와주는 프로그램) 설정 중 `PasswordAuthentication`을 yes로 변경한 뒤 sshd를 재시작하여 config를 적용한 뒤에 

https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh



```bash
local:~$ ssh ubuntu@ec2-어쩌구-저쩌구-ip-주소.ap-northest-2.compute.amazonaws.com -i chicken-access.pem
Are you sure you want to continue connecting (yes/no)? yes
Enter passphrase for key 'chicken-access.pem':
chicken@server~$ 
```

접속 성공.
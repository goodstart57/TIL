# IPad에서 Terminus를 사용하여 AWS EC2 접속하기

ssh를 제공하며 add-free인 장점이 있는 터미널 [install](<https://termius.com/windows>)

iPad를 구매하여 ssh로 ec2 instance에 접속하기 위해 terminus를 사용



## Host 등록

iTunes를 이용하면 태블릿에 바로 pem파일을 등록할 수 있겠지만

내 경우에는 window 10 버전 terminus를 설치하여 진행했다.



### 1. 설치

iPad의 App Store에는 terminus라고 검색하며 최상단에 나온다

window의 설치 링크 : https://termius.com/windows



### 2. key chain 등록

`menu - key chain - + new key` 접속

Label : 해당 키체인에 내가 붙일 별명

PassPhrase : ssh 접속시 필요한 비밀번호라고 들었는데 나와 동일하게 ec2에 접속할 것이라면 비워둬도 잘 들어가진다

Private Key : 옆에 있는 file으로 불러오기 백날해봐야 안된다. pem 파일을 직접 메모장으로 열어서 `모든 텍스트`를 `수정 없이` 복붙

Public Key : 서버에서 사용하는 것으로 알고있다. 이 역시 비워두었다.



### 3. Host 등록

`Host - + NEW HOST` 접속

Label : 해당 호스트에 내가 붙일 별명

Address : 서버의 도메인, ec2의 경우는 퍼블릭 DNS(IPv4)에 해당

Group : 많은 인스턴스를 접속하는 경우 효율적으로 관리 할 수 있다.

Tag : 아마 그룹과 용도가 비슷한 것으로 보인다, 검색할때 사용가능할 것 같다



SSH : on

Port : 기본적으로 22, 다르게 설정해두었다면 해당 port

Username : 해당 계정명, ec2의 경우 putty 접속시 퍼블릭 DNS(IPv4)앞에 username@을 붙여서 접속할텐데 이때 username을 작성하면된다. ubuntu instance의 경우에는 ubuntu가 username으로 설정되어있다.

Password : 아까 생성한 Key Chain 불러오기



### 4. Sync

`왼쪽 최상단 menu - Sync now` 누르기

자신의 태블릿에 접속해보면 굳이 새로고침을 하지 않더라도 host가 등록된 것이 보인다.

접속 성공!
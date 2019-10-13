### App Dev: Setting up a Development Environment - Python

#### Objectives

- VM을 생성하는 Google Compute Engine으로 Google Cloud Platform에서 Python 개발환경 구축
- 소프트웨어 개발을 위해 라이브러리 설치
- 작업 목록
  1. Google Compute Engine  인스턴스 생성 확인
  2. SSH로 인스턴스 접속
  3. 인스턴스에서 파이썬 라이브러리 설치
  4. 소프트웨어 설치 확인

#### Overview

##### Google Cloud Platform; GCP

GCP는 하드디스크나 메모리같은 물리적인 장치, 가상 리소스, VM으로 이루어져 있으며 이것들은 구글 데이터센터에 있습니다.

##### Projects

프로젝트는 설정, 권한, 메타데이터로 이루어져있습니다. 이러한 정보를 공유할 때는 외부 네트워크를 이용할 수 밖에 없습니다.

##### GCP Projects

GCP 프로젝트는 프로젝트 이름, ID, 번호가 있으며 이러한 정보를 이용하여 API를 호출할 수 있습니다.

#### 

#### Set Up

##### VM 생성하기

1. (클라우드 계정 및 프로젝트 생성 완료 후에) 콘솔에 접속해서 네비게이션 메뉴 > Compute Engine > `VM instance` 접속
2. `Create Instance` 버튼을 통해 인스턴스 생성
3. 인스턴스 생성
   - 이름 : dev-instance
   - 리전 : us-central1-a
   - Identity and API access : Allow full access to all Cloud APIs
   - Firewall : Allow HTTP trrafic
4. `VM instances` 페이지에서 `SSH` 클릭하여 인스턴스 접속

##### VM 인스턴스에서 소프트웨어 설치

1. `sudo apt-get update`

   패키지 업데이트

2. `sudo apt-get install git`

   깃 설치

3. `sudo apt-get install python-setuptools python-dev build-essential`

   파이썬 셋업

4. `sudo easy_install pip`

   파이썬 패키지 매니저인 pip 설치



#### Configure the VM to Run Application Software

##### 설치 확인

1. `python --version`

   파이썬 설치 확인

2. `pip --version`

   pip 설치 확인

3. `git clone https://github.com/GoogleCloudPlatform/training-data-analyst`

   깃 저장소 복제

4. `cd ~/training-data-analyst/courses/developingapps/python/devenv/`

   현재 위치 이동

5. `sudo python server.py`

   웹서버 시동

6. VM Instance 리스트 (Navigation menu > Compute Engine > Virtual Instances)에 나와있는 `External IP`에 웹브라우저로 접속하면 `Hello GCP dev`라고 출력

7. `Ctrl + c`로 서버를 종료

8. `sudo pip install -r requirements.txt`

   Google Cloud Engine VM 인스턴스 리스트를 보기 위해 필요한 파이썬 라이브러리 설치

9. `python list-gce-instances.py <PROJECT_ID> --zone=<YOUR_VM_ZONE>`

   - PROJECT_ID : VM instances 등 프로젝트 패키지에서 Google Cloud Platform이라는 로고 오른쪽에서 확인
   - YOUR_VM_ZONE : VM instances에서 Zone 확인

10. 결과

    - `dev-instance`

    
# [Debug] Jupyter Lab/Notebook에서 에러났을 때 해결 기록

## Kernel 연결이 안될때

### Error 출력 로그

```
[E 15:41:28.680 LabApp] Uncaught exception GET /api/kernels/d9598097-d6e4-4b06-a5a9-d3cecf66ab5e/channels?session_id=f6ebb170-037c-44a2-8814-bcacb6798adf (221.143.255.78)
     HTTPServerRequest(protocol='http', host='', method='GET', uri='', version='HTTP/1.1', remote_ip='221.143.255.78')
     Traceback (most recent call last):
     File "/home/jfrost/.local/lib/python3.6/site-packages/tornado/websocket.py", line 546, in _run_callback
     result = callback(*args, **kwargs)
     File "/home/jfrost/.local/lib/python3.6/site-packages/notebook/services/kernels/handlers.py", line 274, in open
     self.create_stream()
     File "/home/jfrost/.local/lib/python3.6/site-packages/notebook/services/kernels/handlers.py", line 127, in create_stream
     meth = getattr(km, 'connect_'   channel)     AttributeError: 'MappingKernelManager' object has no attribute 'connect_control' 
```

### 조치 방법

1. tornado 패키지를 5.1.1 버전으로 다운/업그레이드

2. jupyter-client, jupyter-core 모듈 업데이트


AWS Ec2로 Ubuntu 18 인스턴스를 생성하고 새로운 계정을 만들어 사용하려는데 
python3 명령어가 전혀 듣지 않는 문제가 생겼다. 
(기존 계정에서는 잘 되었음)

둘 중 2번 방법에서 해결되었다.



## 화면(아이콘 등)이 제대로 출력되지 않는 문제

### 조치 방법

1. pip3 freeze | grep jupyter > requirements.txt

2. pip3 install -U -r requirements.txt


AWS Ec2로 Ubuntu 18 인스턴스를 생성하고 새로운 계정을 만들어 사용하려는데 
아이콘이 실종된 상태로 주피터 화면이 띄워졌다.
jupyter 화면을 빌드할 때 nodejs가 문제라는 메세지가 있어서 찾아보았더니
jupyter가 가너무 옛날 버전이라서 생긴 이슈였다.
~~(오랜만에 본다고 조인트 까인 기분이다..)~~


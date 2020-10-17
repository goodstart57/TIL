# Jupyter 설정(Config)



## 1. config 파일 생성

```shell
$ jupyter notebook --generate-config
Writing default config to: [User경로]\.jupyter\jupyter_notebook_config.py
```



## 2. Jupyter 설정

### 일반 설정

#### 작업경로 변경

```
c.NotebookApp.notebook_dir = [원하는 경로]
```



#### 비밀번호 설정

```python
from notebook.auth import passwd
passwd("내_비밀번호")
```

위 코드를 통해 내_비밀번호를 python으로 실행하면 암호화된 내 비밀번호가 출력된다.

```
c.NotebookApp.password = [암호화된_내_비밀번호]
```

암호화되어 `암호화유형:솔트값:암호화된_비밀번호` 형태로 보이는데 출력된 문자열 전부를 ( ' 제외) 써주면 된다.



### Jupyter 서버 설정

#### ip, 포트 변경

```
c.NotebookApp.ip = [원하는 ip/hostname]
c.NotebookApp.port = [원하는 포트]
```

* 허용된 ip/포트를 사용해야 정상적으로 사용 가능
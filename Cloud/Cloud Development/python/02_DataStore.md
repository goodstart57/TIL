### App Dev: Storing Application Data in Cloud Datastore - Python

>
> Qwiklabs 사이트의 Cloud Development 학습입니다.
>
> https://run.qwiklabs.com/focuses/1076?parent=catalog
> 
> 본 문서의 환경은 위 링크의 페이지를 기반으로 발급된 id에서 진행되어야합니다. 
>

#### Overview

`Google Cloud datastore`는 NoSQL document database

- 특징

    1. auto scaling

    2. 높은 수행률

    3. 개발이 쉬움


#### Objectives

1. 개발 환경으로써 Cloud Shell 활용

2. 어플리케이션 미리보기

3. 클라우드 데이터스토어를 통합하기 위해 어플리케이션 코드 갱신


#### Prepare

1. Clone source code

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

2. Change current directory 

```
cd ~/training-data-analyst/courses/developingapps/python/datastore/start
```

3. Set project id to environment variable

```
export GCLOUD_PROJECT=$DEVSHELL_PROJECT_ID
```

4. Install required library

```
sudo pip install -r requirements.txt
```

5. Run Application

```
python run_server.py
```


#### 내려받은 소스코드 확인

GCP Console의 Cloud Shell에서 `Launch Code Editor` 아이콘 클릭하면 파일 체계가 나옵니다.

`/training-data-analyst/courses/developingapps/python/datastore/start` 경로에 가면 `Quiz` 어플리케이션을 확인할 수 있습니다.

> Quiz 어플리케이션은 `Flask` 프레임워크로 작성되어 있습니다.

- ...run-server.py

    이 어플리케이션의 Entry Point를 포함하고 있으며, 파일 실행 시 8080 포트에서 **서버가 동작**합니다.

- ...quiz/init.py

    웹 어플리케이션과 REST API를 위한 **라우트**를 가져옵니다.

- ...quiz/webapp/questions.py and ...quiz/webapp/routes.py

    웹어플리케이션에서 화면을 보여주고 퀴즈를 저장하는 핸들러와 URI를 대칭시키는 라우트가 정의되어있습니다.

- ...quiz/webapp/templates folder.

    Jinja2 형식을 사용하는 웹어플리케이션 사용자 인터페이스를 위한 template을 가지고 있습니다.

- ...quiz/webapp/templates/add.html

    질문 양식 생성을 위한 Jinja2 template

    `퀴즈를 선택하는 선택목록`, `사용자가 질답을 입력할 수 있는 텍스트상자` 그리고 `정답을 선택할 수 있는 라디오 버튼` 세가지에 주목해야합니다.

- ...quiz/api/api.py

    JSON 데이터를 시험치는 학생에게 전달하는 핸들러

- ...quiz/gcp/datastore.py

    Cloud Datastore에서 퀴즈 질문들을 저장하고 불러오는 Datastore 코드
    
    이 모듈은 웹어플리케이션과 API에 불러와집니다.


#### update datastore.py

##### setting variable

```python
import os

# GCLOUD_PROJECT라는 이름의 환경변수 불러오기
project_id = os.getenv('GCLOUD_PROJECT')

from flask import current_app

# google.cloud 패키지의 datastore 모듈 불러오기
from google.cloud import datastore

# Cloud Datastore 클라이언트 객체 생성
# 환경변수에서 불러온 프로젝트 ID를 입력 
datastore_client = datastore.Client(project_id)
```

#####  Datastore에서 load

```python
"""
주어진 주건에 의해 필터링된 질문 개체들의 리스트 반환
- 질문 이름에 의해 필터링 되고, 기본값은 'gcp'
- 페이지 없음
- id 프로퍼티로써 개체 키에 추가
- redact==True => 각 개체의 correctAnswer 프로퍼티를 삭제 
"""
def list_entities(quiz='gcp', redact=True):
    query = datastore_client.query(kind='Question')
    query.add_filter('quiz', '=', quiz)
    results = list(query.fetch())
    for result in results:
        result['id'] = result.key.id
    if redact:
        for result in results:
            del result['correctAnswer']
    return results
```

##### Datastore에 save

```python
"""
각 질문에 대한 생성과 유지와 개체
Datastore key는 RDB의 기본 키와 동일
key를 작성하는 두가지 방법
1. 종류를 지정하고, Datastore가 고유한 숫자 id를 생성
2. 종류와 고유한 문자열 id 지정
"""
def save_question(question):
    # Datastore 개체의 key 생성 (Question 종류)
    key = datastore_client.key('Question')
    # key를 이용하여 Datastore entity object 생성
    q_entity = datastore.Entity(key=key)

    for q_prop, q_val in question.iteritems():
        q_entity[q_prop] = q_val
        datastore_client.put(q_entity) # 저장
```

#### 웹어플리케이션 테스트

1. GCP Console의 Cloud Shell에서 Run Application(`python run_server.py`)

2. `Web preview > Preview on port 8080`에서 웹페이지를 실행

3. `Create Question`에서 원하는 질문 등록, `Take Test`에서 등록된 질문 테스트


#### 저장된 질문 Datastore에서 확인

`GCP Console > Navigation > Datastore > Entities` 에서 확인 가능

## MapReduce

대용량 데이터를 분산처리하기 위해 만들어진 프레임워크

- Mapper와 Reduce라는 기본 단위로 데이터 처리

- Key - Value로 구성된 입출력이 핵심
  - Map : 산재된 데이터를 연관성있는 key-value 형태로 묶는 작업
  - Reduce : 맵 작업 결과에서 중복 데이터 제거 후 원하는 데이터 추출
- 하둡에서 잡은 1:n으로 실행
  - 1 : 잡트래커, 태스크 트레커가 수행할 각각의 태스크를 스케줄링해 시스템 내에서 수행하는 모든 잡이 실행되도록 조절하는 역할
  - n : 태스크 트래커, 각각의 태스크를 수행한 후, 각각의 실행 결과를 잡트레커에 보내는 역할

### 프로세스

1. Input

   - HDFS에서 파일 불러오기
   - (String); "Deer Bear River\nCar Car River\nDeer Car Bear" 문자열 파일 입력

2. Splitting

   - 대용량 파일을 블록 크기가 되도록 분할
   - (key1, val1);  "Deer Bear River", "Car Car River", "Deer Car Bear" 로 쪼개기

3. Map : 입력 파일을 한 줄씩 읽어서 key-value 형태로 변형

   - 분석 대상만을 추출하고 필요없거나 잘못된 레코드를 제거
   - 변형 규칙은 개발자가 정의

   - List(key2, val2); Dear: 1, Bear: 1, River: 1 / Car: 1, Car: 1, River: 1 / Deer: 1, Car: 1, Bear: 1

4. Shuffling

   - Partitioner가 Reduce Task 개수만큼 생성되어 MapTask의 결과를 ReduceTask에서 사용할 수 있도록 병합
   - (key2, List(val2)); Bear: 1, Bear: 1 / Car: 1, Car: 1, Car: 1 / Deer: 1, Deer: 1 / River: 1, River: 1

5. Reduce : Map의 결과를 집계하여 원하는 값을 추출

   - 중복된 값을 제거

   - (key3, val3); Bear: 2 / Car: 3 / Deer: 2 / River: 2

6. Final result

   - Reduce 결과를 통합하여 HDFS에 저장
   - 순차적으로 수행된 MapTask의 결과값들이 모두 처리되면 Reduce에서 일괄적으로 통합
   - List(key3, val3); Bear: 2, Car: 3, Deer: 2, River: 2

   

#### 구성

- HDFS에 저장된 데이터를 처리하여 다시 HDFS에 저장

- MasterNode : SlaveNode = 1 : n
  - MasterNode : Job Tracker와 Name Node로 구성
  - SlaveNode : Task Tracker와 Data Node로 구성
  - 각각의 TaskTracker는 MapTask, ReduceTask 수행
- JobTracker와 TaskTracker는 하트비트 메소드를 이용하여 통신
  - MapTask, ReduceTask 수행시 JVM 상에서 돌아감
  - JVM은 여러개 사용할 수 있고 재사용 가능
  - JobTracker : 전체 Job을 모니터링
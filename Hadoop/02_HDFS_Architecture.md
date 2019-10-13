---
layout : post
title : HDFS Architecture
date : 2019.08.13
author : JAESEO LEE
---

## HDFS Architecture

하둡 프레임 워크의 파일 시스템을 위해 만든 시스템으로 대용량 파일을 분산된 서버에 저장한다.

### 목표

1. 장애 복구 - 네트워크 상의 문제가 생겼을 때에도 대처 가능
2. 스트리밍 방식의 데이터 접근
3. 대용량 데이터 저장
4. 데이터 무결성

### 특징

- 마스터 노드(네임 노드) 하나와 여러개의 슬레이브 노드(데이터 노드)로 구성

  -  Master Node : Job Tracker - Task를 Slave Node에 분산

  - Slave Node : Task Tracker

- 저사양의 서버를 이용하여 스토리지 구성 가능
  - NAS (안정성), DAS, SAN(고성능) 비해 비용적인 장점
- 블록 구조의 파일 시스템
  - 관리하는 블록의 수가 대폭적으로 줄어서 메인 노드에 할당된 메모리를 효율적으로 관리
  - 탐색 시간(seek time + search time)이 64MB 일때 가장 빨라서 64MB로 설정
  - Hadoop 2.0부터 블록의 크기가 64MB에서 128MB로 증가
- 전자상거래와 같은 안정성이 중요한 서버에는 부적합



### 네임 노드

- 메타데이터 관리
- 데이터노드 모니터링
- 블록 관리
- 클라이언트 요청 접수

### 데이터 노드

- 클라이언트가 저장한 파일을 로컬 디스크에 유지
- 로우 데이터와 메타데이터(파일 생성일자, 체크섬 등) 두가지로 저장



### HDFS에 200MB 데이터 저장 과정

1. Block 1, 2, 3에 64MB, Block 4에 8MB 저장

2. 여러개의 노드에 각 블록이 각각 3번(기본값)씩 저장된다

   예) Node 1 (Block 1, 2, 3), Node 2 (Block 2, 3, 4) Node 3 (Block 1, 2, 4), Node 4 (Block 1, 3, 4)



### HDFS의 데이터 전송 과정

1. Client에서 저장 요청 : `write()`
2. DistributedFileSystem이 DFSClient가 DFSOutputStream 객체 생성하도록 명령
3. 네임노드에서 생성된 DFSOutputStream 객체 `유효성 검사`
4. 클라이언트와 네임노드간의 통신을 통해 `스트림(DFSOutputStream) 객체 생성`
   - DFSOutputStream : DataStreamer thread + Response Processor thread
5. 이 스트림을 통해 파일을 각 데이터노드에 패킷 단위로 전송
   - `addBlock()` : DataSreamer가 Name Node에 블록 저장 요청
   - Name Node가 Data Streamer에게 `Data Node 목록 반환`
   - Data Node의 DataXceiver Server 동작하여 클라이언트로부터 패킷 전달 받으며 다른 데이터노드들과 파이프라인 구축
     - 패킷 전달 과정에서 장애가 발생하면 새로운 데이터노드 목록을 받아서 새로운 파이프라인에서 장애가난 노드부터 재전송
   - 데이터 저장이 승인되면 `Ack Message`가 Response Processor로 전달
   - 마지막 데이터노드가 저장 완료 결과 전달 : `blockReceiver`
6. 파일 전송이 완료되고 나서, 클라이언트에서 스트림을 close하면 남은 패킷이 Flush
7. 클라이언트에서 네임노드의 `complete()`를 호출하여 정상적으로 저장되었다면 true 반환 (저장 성공)
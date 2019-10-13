---
layout : post
title : HDFS Architecture2
date : 2019.08.13
author : JAESEO LEE

---

## HDFS Architecture2

### HDFS의 파일 읽기

1. 클라이언트에서 요청 : `read()`

2. `DFSClient`의 `open()` 호출하여 `DFSInputStream` 객체 생성

   - 클라이언트에서 스트림 객체에 블록 리더기 생성
     - 블록과 저장된 데이터노드가 같은 서버 : `BlockReaderLocal`
     - 블록과 저장된 데이터노드가 원격 서버 : `RemoteBlockReader`

   - `open()`호출시 `DFSDataInputStream`이 `DFSInputStream`을 래핑한다.
     - *래핑?*

3. DFSInputStream이 모든 블록을 읽는다.

   - 기본 블록 사이즈의 10배만큼 탐색

   - `BlockReaderLocal` : 데이터노드에서 직접 읽기
   - `RemoteBlockReader` : 데이터노드 내의 `DataXceiver Server`에서 읽기

4. DSClient가 네임노드에게 불러올 파일의 블록 위치 요청 : `getBlockLocations()`

5. 네임노드가 DFSClient에게 블록 위치 반환
   - 네임노드는 블록 위치 목록을 생성하고 클라이언트에 가까운 순서대로 정렬하여 성능 향상

   - *클라이언트에 가까운 순서가 어떤 순서일까?*

6. 모두 읽고난 후에 블록 리더기 닫고 원격 노드와 커넥션 종료 : `close()`


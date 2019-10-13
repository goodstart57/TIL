---
layout : post
title : HDFS Name Node
date : 2019.08.13
author : JAESEO LEE
---

## HDFS Name Node

### Secondary Name Node

- 장애 발생시 대처하기 위해 백업기능 제공 : `체크포인트`
  - 서버가 리부팅되면 네임노드가 메모리에서 처리하는 메타데이터 손실 가능성
  - `HDFS`에서는 `editslog`와 `fsimage` 두개 파일 생성
    - `editslog` : 모든 변경 이력 저장
    - `fsimage` : 메모리에 저장될 메타데이터의 파일시스템 이미지 저장한 파일
    - editslog가 커지면 simage 만드는데 시간이 많이 소요된다.
- 보조네임노드는 fsimage를 줄여주는 역할을 한다.
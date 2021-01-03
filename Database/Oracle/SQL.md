# SQL (Structured Query Language)

데이터베이스를 제어하기 위한 언어로 크게 DDL, DML, DCL로 나뉘어 진다.

DB 종류에 따라 SQL의 차이가 있지만, `SELECT ... FROM ... ;`와 같이 공통적으로 사용하는 부분도 있다.



## DDL

데이터베이스의 SCHEMA, DOMAIN, TABLE, VIEW, INDEX 를 조작하기 위한 언어



### CREATE USER

```SQL
CREATE USER [username] IDENTIFIED BY [password]
DEFAULT tablespace [tablespace name]
TEMPORARY tablespace [temp tablespace name]
;

CREATE USER chicken identified by cock
DEFAULT tablespace USERS
TEMPORARY tablespace TEMP
;
```

- username : 유저이름으로 oracle 12c 이후부터 c##으로 시작하는 이름을 써야한다. 예외 적용을 하고 싶다면, `ALTER SESSION SET "_ORACLE_SCRIPT"=true; `로 세션변경 후 계정생성하면 된다.
- `GRANT ROLE`명령어를 통해서 권한을 설정해야 한다.



### GRANT

```SQL
GRANT [role1, role2, ...] TO [username];

GRANT connect, resource, dba to checken;
```





## DML

데이터를 조작하기 위한 언어



### INSERT



### SELECT



### UPDATE



### DELETE





## DCL

데이터를 제어하는 언어

데이터의 보안, 무결성, 회복, 병행 수행제어 등을 정의하는데 사용한다.



### COMMIT



### ROLLBACK









출처: https://parkbosung.tistory.com/11 [IT 지식 쌓기]
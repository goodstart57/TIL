# Database

## RDMBS

관계형 데이터베이스 관리 시스템

Relational Database management system

> 왜 Relational 인가?
>
> 데이터를 행과 열을 통해서 조작하겠다.

### RDBMS 종류

1. MySQL
2. PostgreSQL
3. Oracle



### RDBMS 용어

**스키마** : 데이터베이스에서 자료의 구조, 표현방법, 관계, 제약조건 등을 정의한 구조

**열(Column)** : 각 열에는 고유한 데이터 형식이 지정된다(INTEGER, TEXT, NULL, etc...)

**행(row, 레코드)** : 테이블의 데이터는 행에 저장된다. (User테이블에 4명의 고객정보가 저장되어 있다면 4행)

**PK(기본키)** : 각 행의 고유값으로  Primary Key로 불린다. 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.



### Sqlite3 해보기

#### csv 파일으로 테이블 만들기

```sqlite
.import assets/data/hellodb.csv hellodb
.tables
```



#### 테이블 데이터 쿼리하기

**모든 데이터 쿼리**

```sqlite
SELECT * FROM hellodb;
```

**output**

```
1,길동,홍,600,충청도,010-2424-1232
```



**특정 컬럼 쿼리**

```sqlite
SELECT age FROM hellodb;
```





**컬럼 사이에 tapping**

```sqlite
.mode column
```



**컬럼명 출력**

```sqlite
.headers on
```



#### 데이터베이스(스키마) 만들기

```
$ sqlite3 tutorial.sqlite3
```

```sqlite
.databases
```

데이터베이스를 만들고난 후에 `.databases` sqlite3 명령어를 통해 파일로 저장한다.

sqlite3의 확장자는 `sqlite3`혹은 `db`를 사용한다.



#### 테이블 만들기

```sqlite
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
    name TEXT
);
```

`id`와 `name`컬럼이 있는 `classmates` 테이블 만들기



> classmates와 같이 복수형으로 쓰는 것을 권장한다.



**스크립트 파일을 통해서 만들기**

위 코드를 `create_talbe.sql` 파일로 생성한 뒤에 

```sqlite
.read create_table.sql
```

을 통해 스크립트를 실행한다.





**테이블이 잘 만들어졌는지 조회**

```sqlite
.tables
.schema classmates
```

#### sqlite 데이터 타입

1. INTEGER
2. TEXT
3. REAL
4. NUMERIC
5. BLOB -- 파일 뭉치

INTEGER에 TINYINT(1byte), SMALLINT(2bytes), MEDIUMINT(3bytes) 등 많은 세부 데이터 타입이 있지만, 서비스 단계에서 구현!



#### 테이블 제거

```sqlite
DROP TABLE classmates;
```



**새로운 테이블 만들기**

```sqlite
CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	name TEXT
);
CREATE TABLE classmate (
	id INTEGER PRIMARY KEY,
	name TEXT,
    age INTEGER,
    address TEXT
);
```



#### 새로운 행 저장하기

```sqlite
INSERT INTO classmates (name, age) VALUES ('이재서', "27");
INSERT INTO classmates (name, age) VALUES ('이재서', "27");
```

```
1|이재서|27|
2|홍길동|23|
```

`id`는 자동으로 입력된다. 즉, `primary key`는 자동으로 입력된다.



```sqlite
INSERT INTO classmates (id, name, age) VALUES (2, '이재서', "27"); 
```

```
UNIQUE constraint failed: classmates.id
```

강제로 id를 지정해서 넣어보면 id가 중복되어 실패했다는 메세지가 출력된다.



```sqlite
INSERT INTO classmates VALUES ('홍길동', '30', '서울');
```

```
Error: table classmates has 4 columns but 3 values were supplied
```

컬럼명 생략시 id를 포함한 모든 컬럼의 데이터를 넣어야 한다. 따라서 ,

```sqlite
INSERT INTO classmates VALUES (3, '홍길동', '30', '서울');
```

여기서 `classmates` 테이블을 쿼리해보면 다음과 같다.

```
id          name        age         address   
----------  ----------  ----------  ----------
1           이재서   27                    
2           홍길동   23                    
3           홍길동   30          서울
```

id가 1, 2에 해당하는 address는 주소가 비어있고, 이러한 구조는 좋지 않다. 따라서 NULL 값을 용인하지 않기 위해서 `NOT NULL` 구문을 추가합니다.

```sqlite
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT DEFAULT "homeless"
);
```



```sqlite
INSERT INTO classmates (name, age, address) VALUES ("이재서", 28, "서울");
INSERT INTO classmates (name, age, address) VALUES ("손지명", 29, "서울");
INSERT INTO classmates (name, age, address) VALUES ("민경욱", 30, "평양");
```



#### 테이블 쿼리 - LIMIT, OFFSET (일부 조회하기)

```sqlite
SELECT id, name, age FROM classmates LIMIT 1;
SELECT id, name, age FROM classmates LIMIT 1 OFFSET 1;
SELECT id, name, age FROM classmates LIMIT 2 OFFSET 1;
```

게시판에서 한 페이지당 게시글 20개씩 보여주기로 했다.

이때 `LIMIT 20 OFFSET (현재 페이지-1)*20`으로 쿼리하는 경우 원하는 페이지의 게시글을 불러올 수 있다.



#### 테이블 쿼리 - WHERE (조건 검색)

```sqlite
SELECT id, name, age FROM classmates WHERE name = "이재서";
```



#### 행 삭제했다가 다른 값으로 추가하면???

```sqlite
SELECT * FROM classmates;
DELETE FROM classmates WHERE name = "이재서";
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ("마근호", 30, "강릉");
SELECT * FROM classmates;
```

```
id          name        age         address   
----------  ----------  ----------  ----------
2           손지명   29          서울    
3           민경욱   30          평양    
4           이재서   28          서울

id          name        age         address   
----------  ----------  ----------  ----------
2           손지명   29          서울    
3           민경욱   30          평양  

id          name        age         address   
----------  ----------  ----------  ----------
2           손지명   29          서울    
3           민경욱   30          평양    
5           마근호   30          강릉
```

id=4인 이재서가 삭제되



### 새로운 DB 생성 및 csv 파일에서 테이블 불러오기

```
$ sqlite3 users.sqlite3
```

```sqlite
.database
.mode csv
.import assets/data/users.csv users
.tables
.schema users
```

```
CREATE TABLE users(
  "id" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" TEXT,
  "country" TEXT,
  "phone" TEXT,
  "balance" TEXT
);
```



#### 테이블의 행의 수를 알아보자

```sqlite
SELECT COUNT(*) FROM users;
```



#### 좀더 어려운 쿼리문을 해보자

잔고가 가장 많은 사람 조회하기

```sqlite
SELECT last_name, first_name, MAX(balance) from users;
```

30대 평균 연봉

```sqlite
SELECT AVG(balance) FROM users WHERE age >= 30;
```

#### 테이블 쿼리 - WHERE + LIKE

| LIKE 표현식 | 뜻                             |
| ----------- | ------------------------------ |
| 2%          | 2로 시작                       |
| %2          | 2로 끝                         |
| %2%         | 2가 포함된                     |
| _2%         | 2번째 자리가 2인               |
| 1___        | 첫번째 자리가 1이고 4자리 글자 |
| 2\_%\_%     | 2로 시작하며 3자리인 글자      |



#### 산술연산도 가능하다

```sqlite
SELECT AVG(age) FROM users
```

age에는 숫자형 컬럼만 들어갈 수 있고

AVG대신 MIN, MAX 등 산술 연산이 가능하다.



#### 정렬해보자 (오름차순, 내림차순)

```sqlite
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age DESC LIMIT 10;
```



나이가 적고, 이름순으로 정렬시킨 후 10개만 뽑기

```sqlite
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```



잔고 TOP 10 불러오기

```sqlite
SELECT * FROM users ORDER BY balance DESC LIMIT 10;
```

```
627,"선영","김",37,"전라북도",02-1610-2940,990000
124,"상현","나",30,"경상북도",010-4571-2869,99000
235,"정호","이",20,"전라북도",011-1193-3920,99000
259,"상철","이",17,"전라북도",011-3990-3978,99000
500,"지아","최",16,"전라북도",02-4150-9018,9900
768,"준서","박",17,"전라남도",010-9213-9802,9900
296,"미영","문",31,"전라남도",016-3620-8275,980000
327,"하윤","고",32,"제주특별자치도",02-7876-4073,980000
357,"은정","유",17,"강원도",016-8867-7897,980000
751,"서윤","안",29,"경상남도",011-2018-8263,98000
```

?? 이상하다

```
sqlite> .schema users
CREATE TABLE users(
  "id" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" TEXT,
  "country" TEXT,
  "phone" TEXT,
  "balance" TEXT
);
```

모든 컬럼이 TEXT로 되어있다.


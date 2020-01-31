# 순위메기기 (RANK, DENSE_RANK, ROW_NUMBER)

## RANK, DENSE_RANK, ROW_NUMBER
- RANK : 동일한 값을 가진 행들은 동일한 순위를 가지며 다음 순위는 해당 개수만큼 건너뛰어 메긴다
- DENSE_RANK : 동일한 값을 가진 행들은 동일한 순위를 가지며 다음 순위는 해당 개수만큼 건너뛰지 않고 메긴다
- ROW_NUMBER : 각각의 행에 할당된 연속적이며 고유한 정수 -> 순차적으로 숫자를 메긴다

```sql
SELECT AGE
     , RANK() OVER(ORDER BY AGE) AS EX_RANK
     , DENSE_RANK() OVER(ORDER BY AGE) AS EX_DENSE_RANK
     , ROW_NUMBER() OVER(ORDER BY AGE) AS EX_ROW_NUMBER
  FROM EMPLOYEES
;
```

AGE | EX_RANK | EX_DENSE_RANK | EX_ROW_NUMBER
----|---------|---------------|---------------
25  |    1    |       1       |      1
27  |    2    |       2       |      2
27  |    2    |       2       |      3
27  |    2    |       2       |      4
28  |    5    |       3       |      5
30  |    6    |       4       |      6
# Text File

method to process text file in python

## Diff between FILE and DB

__File__

1. file open
2. file read/write/edit(append)
3. file close

save very small data like variable

__csv__ --> 2d-list

- open csv file (import csv)
- 1. read 
- 2. write 
- 3. edit (append)
- close csv file


__json__ --> dictionary

- open .json file (import json)
- 1. read 
- 2. write 
- 3. edit (append)
- close json file

__DB__ 

1. open (connect) -> CRUD
2. read(CREATE)/write(READ/RETIEVE)/edit(UPDATE)/remove(DELETE/DESTROY)
3. close(disconnect)

```python
# With `with` keyword, you can use briefly

with open('./my_text.txt', 'r') as f:
    f.write('added line')
    f.close()
```

dictionary(key-value) +  강력한 메소드 추가 = object

=> ORM

## Example for CSV

`csv` library can write csv file easily by doing list.

### Write

```python
import csv

f = open('ssapy1.csv', 'w', encoding='utf-8')
ssapy1 = csv.writer(f)
ssapy1.writerow(['name', 'email', 'phone', 'group', 'major'])
f.close()
```

output file
```
name,email,phone,group,major
```

### Add

```python
import csv

f = open('ssapy1.csv', 'a', encoding='utf-8')
ssapy1 = csv.writer(f)
ssapy1.writerow(['JAESEO LEE', 'goodstart57@gmail.com', 'no', 'ssapy', 'statistics'])
f.close()
```

output file

```
name,email,phone,group,major

JAESEO LEE,goodstart57@gmail.com,no,ssapy,statistics

```

### Read

```python
import csv

f = open('ssapy1.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f, delimiter=',')
for row in csv_reader:
    print(row)
f.close()
```

output
```
['name', 'email', 'phone', 'group', 'major']
[]
['JAESEO LEE', 'goodstart57@gmail.com', 'no', 'ssapy', 'statistics']
[]
```

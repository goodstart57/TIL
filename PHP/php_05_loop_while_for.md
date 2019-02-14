# Loop (for, while) in PHP

## Kinds of Loops

- while
- do...while
- for
- foreach



## While

### Syntax

```
while (condition is true) {
    code to be executed;
}
```

### Ex

```php
<?php 
$x = 1; 

while($x <= 5) {
    echo "The number is: $x <br>";
    $x++;
} 
?>
```

```
The number is: 1 
The number is: 2 
The number is: 3 
The number is: 4 
The number is: 5 
```



## do ... while

### Syntax

```
do {
    code to be executed;
} while (condition is true);
```

Difference with `while` is `do while` run `code to be executed;` part once anytime.



## for

### Syntax

```
for (init counter; test counter; increment counter) {
    code to be executed;
}
```



### Ex

```php
<?php 
for ($x = 0; $x <= 10; $x++) {
    echo "The number is: $x <br>";
} 
?>
```

```
The number is: 0 
The number is: 1 
The number is: 2 
The number is: 3 
The number is: 4 
The number is: 5 
The number is: 6 
The number is: 7 
The number is: 8 
The number is: 9 
The number is: 10 
```



## foreach

### Syntax

```
foreach ($array as $value) {
    code to be executed;
}
```

### Ex

```php
<?php 
$colors = array("red", "green", "blue", "yellow"); 

foreach ($colors as $value) {
    echo "$value <br>";
}
?>
```

```
red 
green 
blue 
yellow 
```


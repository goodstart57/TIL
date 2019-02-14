# Variable in PHP

## declare variable

```php
<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;

echo $txt;
echo $x;
echo $y;
?>
```

```
Hello world
5
10.5
```

`txt`, `x`, `y`라는 변수에 각각 문자열, 정수, 실수를 저장하고

`echo`함수로 저장된 값을  확인한다.



## echo, print

변수를 출력할때 사용되는 함수는 `echo`, `print` 이다.

php에서 echo, print는 `(`, `)`를 사용하지 않는다.

```php
<?php
$txt1 = "W3Schools.com";
$x = 5;
$y = 4;

echo "Hello world!<br>";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
echo "Study PHP at " . $txt1 . "<br>";
echo $x + $y;
?>
```

```
Hello world!

This string was made with multiple parameters.
Study PHP at W3Schools.com
9
```



## DataType in PHP

- String
- Integer
- Float
- Boolean
- Array
- Object
- NULL
- Resource



### array

```php
<?php 
$cars = array("Volvo","BMW","Hyundai");
var_dump($cars);
?>
```

```
array(3) { [0]=> string(5) "Volvo" [1]=> string(3) "BMW" [2]=> string(7) "Hyundai" }
```



### object (class)

```php
<?php
class Car {
    function Car() {
        $this->model = "VW";
    }
}
// create an object
$herbie = new Car();

// show object properties
echo $herbie->model;
?>
```

```
VW
```



### NULL

```php
<?php
$x = "Hello world!";
$x = null;
var_dump($x);
?>
```

```
NULL
```


# Constants in PHP

## Declare Constants

```p
define(name, value, case-insentive);
/*
name : constant name
value : constant value like variable value
case-insentive : if this constant name is HI and case-insentive is true, then can use hi as constant
*/
```



```php
<?php
define("GREETING", "Welcome to W3Schools.com!");

function myTest() {
    echo GREETING;
}
 
myTest();
?>
```

```
Welcome to W3Schools.com!
```


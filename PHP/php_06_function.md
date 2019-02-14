# Function in PHP

## Declare Function (Syntax)

```
function functionName() {
    code to be executed;
}
```

```
function functionName($varname1, $varname2, ...) {
    code to be executed;
}
```



### Ex

```php
<?php
function writeMsg() {
    echo "Hello world!";
}

writeMsg(); // call the function
?>
```

```
Hello world!
```



```php
<?php
function greet($fname) {
    echo "Hi $fname<br>";
}

familyName("JAESEO");
familyName("WOOJUNG");
?>
```

```
Hi JAESEO
Hi WOOJUNG
```


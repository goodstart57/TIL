# Start JAVA in VSC

Visual Studio Code에서 자바 실행시켜보기 [ref](<https://code.visualstudio.com/docs/java/java-tutorial#_before-you-begin>)

## 설치

### 1. JDK 1.8

- [jdk 1.8 설치](<https://www.oracle.com/java/technologies/javase-jdk8-downloads.html>)



### 2. visual studio code

- [vs code 설치](https://code.visualstudio.com/download)

- [java extension pack](<https://github.com/Microsoft/vscode-java-pack>) (해당 확장팩을 vs code내에서 설치)





## 실행

VS Code -  `Ctrl + Alt + P` - `Java: Getting Started` 



### 1. 프로젝트 생성

`FIRST_VSC_JAVA` 폴더생성하여 폴더 열기



### 2. 클래스 생성

`QuickStart.java` 파일 생성

```java
class QuickStart {
    public static void main(String[] args) {
        System.out.println("Hello, World.");
    }
}
```



### 3. 실행

`QuickStart.java` 파일을 열고 `F5`로 실행

```
Hello, World.
```



> Visual Studio Code가 범용성도 좋으면서 가벼워서 사용하기 편리하다...
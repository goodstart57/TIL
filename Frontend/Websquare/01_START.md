# Start Websqaure



## 

![Websquare First Screen](\assets\images\Frontend\Websquare\01_START_Websquare screen.png)





## script

> 전역변수 생성하지 않는다.
>
> 만약 script 초반에 var a = "";와 같이 변수 생성하는 경우 페이지 로드할 때 마다 변수가 생성되어 리소스 낭비가 심하다.



## DataCollection

- DataMap : 단건

- DataList : 다건

- LinkedDataList

  단순 Viewer 용도이며 현재는 DataList와 기능이 비슷해서 거의 사용하지 않는다.

  wframe과 같이 부모-자식 관계인 경우에 사용

- 테스트를 위해 초기데이터 생성 가능



## Source

>Source에서 직접 코딩하는 것은 개발자의 실수가 있을 수 있으므로 권장하지 않는다.
>
>ex) 중요 attribute 삭제 





## Event

scwin.onpageload : 페이지 로드가 끝나고 적용

scwin.init : 컴포넌트가 만들어지기 전에 실행되어 초기값을 적용하기에 적합하지 않음
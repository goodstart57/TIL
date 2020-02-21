# Websquare Component

## Component Attribute

- renderType
  - component  : (defautl) 브라우저에 관계없이 Websquare의 디자인으로 생성
  - navtive : Component의 기본값



## Form Component

### trigger

버튼 만들때 사용

### multiupload

websquare_home\config



## Grid

### Grid

테이블 모양의 화면 만들 때 사용

### GridView

- custom type : 컬럼동작 변경

- DataList를 드래그해서 끌어오면 헤더/바디의 ID를 바인딩

  - 처음 연동 시 "신규 생성"하면 컬럼수에 맞게 GridView의 컬럼을 생성

- width 변경

  - 일일히 변경 시 header 기준으로 변경
  - property의 autoFit을 이용하여 브라우저 크기에 맞춰서 컬럼 크기 수정 가능
  - autoFit은 autoFitMinWidth와 같이 사용하여 컬럼 width가 일정 이하로 줄어들지 않도록 조정

- Column

  - column 삭제

    1. column property의 hidden을 이용하여 감추기 (데이터는 남아있다)

    2. column 자체를 GridView내에서 삭제

  - 컬럼 이동 : property columnMove

  - 필터 : property(column) useFilter, property useFilterList

  - 정렬 : property(GridView, column) sortable

- Property

  - GridView는 GridView자체, Header, Body 각각 Property를 가진다.
    - 이를 통해 컬럼별로 속성 적용 가능
  - filter : 필터링 기능, 정렬(헤더 더블클릭), 다중정렬(Ctrl+더블클릭) 기능 사용 가능
  - DrillDown : 드롭다운 목록 사용 가능
  - autoFit : lastColumn, allColumn, none
  - autoFitMinWidth : 최소화면크기 입력
  - columnMove : true(활성화), false(비활성화)
  - sortable : 더블클릭하면 오름차순, 내림차순, 원본 / ctrl+더블클릭하면 다중 정렬 가능
  - sortEvent : 정렬하는 이벤트를 변경 (onclick, ondbclick)
  - editModeEvent : 수정하는 이벤트를 변경 (onclick, ondbclick)
  - keyMoveEditMode : true(화살표키를 이용하여 이동 시 바로 편집모드 적용)
  - focusFlow : linear(화살표키를 이용하여 마지막컬럼에서 바로 첫 컬럼으로 이동 가능)
  - focusMode : cell(클릭 시 셀 단위로 포커스) , row(클릭 시 행 단위로 포커스)
  - rowNumVisible : true(행 순번 출력)
  - rowNumHeaderValue : 순번 헤더값 입력
  - rowStatusVisible : 입력/수정/삭제 상태 표시, 조회된 상태에는 표시값 없음
  - visibleRowNum : 보이는 행 수 조절

- Property (Column)

  - hidden : true(감추기), false(보이기)
  - inputType : text, number, select, combo 등 
    - select 선택시 DataList로 바인딩 가능
  - viewType : icon(inputType 중 select, calendar와 같은 경우를 식별하기 위해 셀에 아이콘으로 표시)
  - displayFormat : ###-###
  - displayFormatter : 함수명 기입, data를 인자로 받고 data를 반환해야 한다.
  - customFormatter : 셀의 형식을 재설정 가능, text/link/textimage/textarea/select/expression/spinner인 경우에만 사용 가능
    - formatter function 생성 시 data, fData, rowIndex, columnIndex를 인자로 받고 fData를 반환해야한다.
    - fData는 GridView에서 셀의 값이 nobr 혹은 img 태그로 생성되어있는데 이 태그자체를 의미

### Pivot

- Viewer 용 Component
- 컬럼/행/값을 유연하게 변경 가능



## Container

### Group

- div 등으로 하위노드를 가질 수 있는 component를 그릴 때 사용

- attribute
  - tagname : default=div

### Generator

- Grid와 비슷하게 2/3중 컬럼을 가진 테이블을 자유롭게 사용가능

- 난이도 상

### TabContainer

- 지금은 사용하지 않는다.

### TabControl

- TabContainer 대체

### WidgetContainer

- 사용자별로 탭을 개인화 할 수 있다.

### ScrollView

- 스크롤이 스크롤 중에만 보이는 View
- 모바일 환경에서 유용



## Navigation

### Accordion

- 수직으로 hide/show 가능



## Frame

### IFrame

- 독립적인 여러 화면을 각각 한 화면에 로드 가능 (중복 이슈 등 제어 가능)

- 하지만, 한 화면에 4개 화면을 로드하는 경우 유저 입장에서는 한번에 5개 화면을 로드하는 리소스가 필요하므로 성능 이슈 발생 --> 비추천 (SP2 이후 금지)

### WFrame

- IFrame의 성능이슈 해결하기위해 나온 Frame (SP2 이후 적용)

- attribute
  - scope



## Chart

### Char

- 거의 사용하지 않는다.

### FusionChart

- 다양한 기능 제공
- 
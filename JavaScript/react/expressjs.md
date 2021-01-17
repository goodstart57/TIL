# Express js로 페이지 만들어보기

[Express hello-world](https://expressjs.com/ko/starter/hello-world.html)

## 환경 구성

### 1. nodejs 설치
[nodejs 설치](https://nodejs.org/ko/download/)
안정적인 LTS 버전으로 설치하도록 한다.

[postman 설치](https://www.postman.com/downloads/)

### 2. express 설치
프로젝트 경로를 생성/이동하고 그 위치에서 express를 설치한다.

```shell
$ mkdir BOILER-PLATE
$ cd BOILER-PLATE
$ npm install express --save
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN boiler-plate@1.0.0 No repository field.

+ express@4.17.1
added 50 packages from 37 contributors and audited 50 packages in 8.664s
found 0 vulnerabilities
```

### 3. project 생성

```shell
$ cd BOILER-PLATE
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (boiler-plate)
version: (1.0.0)
description: first expressjs page
entry point: (index.js)
test command:
git repository:
keywords:
author: goodstart57
license: (ISC)
About to write to C:\Workspace\BOILER-PLATE\package.json:

{
  "name": "boiler-plate",
  "version": "1.0.0",
  "description": "first expressjs page",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "goodstart57",
  "license": "ISC"
}


Is this OK? (yes)
```

## express 프로젝트 구성

```js
// /index.js
const express = require('express')
const app = express()
const port = 3000

// "/" 경로로 요청했을 때 "Hello World!"를 응답한다.
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// 특정 port로 요청 받은 경우 console에 해당 글을 출력
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```

서버 실행

```shell
$ node index.js
Example app listening at http://localhost:3000
```

## mongodb 연결

### mongodb 생성

1. mongodb 회원가입
    - [mongodb homepage](https://www.mongodb.com/)
2. 클러스터 생성
    - free tier이면서 가장 가까운 싱가포르 리전으로 선택
    - 생성에 몇분 소요
    - 생성 후 connect 클릭하여 Connect to Cluster0에 접근
3. Setup connection security
    - ip whitelist는 전세계에 개방 (연습용이니까..)
    - connect에서 user 생성
4. Choose a connection method
    - Connect your application 선택
    - "mongodb+srv://chicken:<password>@cluster0.3vo5a.mongodb.net/<dbname>?retryWrites=true&w=majority"과 방금 생성한 비밀번호를 합쳐서 index.js에서 mongodb 연결을 생성한다.

5. 연결 생성

```javascript
// "/index.js"
const express = require('express')
const app = express()
const port = 3000

var mkey = process.env.mkey
const mongoose = require('mongoose')
mongoose.connect(`mongodb+srv://chicken:${mkey}@cluster0.3vo5a.mongodb.net/<dbname>?retryWrites=true&w=majority`, {
    useNewUrlParse: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
    useFindAndModify: false
}).then(() => console.log('MongoDB Connected...'))
  .catch(err => console.log(err))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```


## MongoDB Model & Schema

```javascript
// "/models/User.js
const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    name: {
        type: String,
        maxlength: 50
    },
    email: {
        type: String,
        trim: true, // 문자열 내 입력된 공백 제거
        unique: 1
    },
    password: {
        type: String,
        maxlength: 50
    },
    role: {
        type: Number,
        default: 0
    },
    image: String,
    // 유효성 관리
    token: {
        type: String
    },
    tokenExp: {
        type: Number
    }
})

const User = mongoose.model('User', userSchema)

module.exports = {User}
```


## Body-parser

### 설치

```shell
$ npm install body-parser --save
npm WARN boiler-plate@1.0.0 No repository field.

+ body-parser@1.19.0
updated 1 package and audited 82 packages in 1.854s

2 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

### Register Route 만들기

```javascript
const express = require('express')
const app = express()
const port = 3000

// [body-parser]
const bodyParser = require('body-parser');
// [model]
const { User } = require('./models/User');

// [body-parser] application/x-www-form-urlencoded 형태의 데이터를 분석해서 가져올 수 있게 세팅
app.use(bodyParser.urlencoded({extended: true}));
// [body-parser] application/json 형태의 데이터를 분석해서 가져올 수 있게 세팅
app.use(bodyParser.json());

// [mongoose]
var mkey = process.env.mkey
const mongoose = require('mongoose')
// [mongoose] mongodb 연결
mongoose.connect(`mongodb+srv://chicken:${mkey}@cluster0.3vo5a.mongodb.net/<dbname>?retryWrites=true&w=majority`, {
    useNewUrlParse: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
    useFindAndModify: false
}).then(() => console.log('MongoDB Connected...'))
  .catch(err => console.log(err))

// [route] index
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// [route] 회원가입
app.post('/register', (req, res) => {
    // 회원가입 정보를 DB에 입력

    const user = new User(req.body) // body-parser 사용됨
    user.save((err, doc) => {
        if(err) return res.json({ success: false, err})
        return res.status(200).json({
            sucess: true
        })
    })
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```

"http://localhost:3000/register"로 올바른 회원가입 정보가 요청되는 경우 "{success : true}"를 응답받는다.

회원가입 정보 예시
```json
{
    "name": "chicken",
    "email": "chicken@gmail.com",
    "password": "1234567"
}
```
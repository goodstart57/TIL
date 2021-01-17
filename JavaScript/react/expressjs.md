# Express js�� ������ ������

[Express hello-world](https://expressjs.com/ko/starter/hello-world.html)

## ȯ�� ����

### 1. nodejs ��ġ
[nodejs ��ġ](https://nodejs.org/ko/download/)
�������� LTS �������� ��ġ�ϵ��� �Ѵ�.

[postman ��ġ](https://www.postman.com/downloads/)

### 2. express ��ġ
������Ʈ ��θ� ����/�̵��ϰ� �� ��ġ���� express�� ��ġ�Ѵ�.

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

### 3. project ����

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

## express ������Ʈ ����

```js
// /index.js
const express = require('express')
const app = express()
const port = 3000

// "/" ��η� ��û���� �� "Hello World!"�� �����Ѵ�.
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// Ư�� port�� ��û ���� ��� console�� �ش� ���� ���
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```

���� ����

```shell
$ node index.js
Example app listening at http://localhost:3000
```

## mongodb ����

### mongodb ����

1. mongodb ȸ������
    - [mongodb homepage](https://www.mongodb.com/)
2. Ŭ������ ����
    - free tier�̸鼭 ���� ����� �̰����� �������� ����
    - ������ ��� �ҿ�
    - ���� �� connect Ŭ���Ͽ� Connect to Cluster0�� ����
3. Setup connection security
    - ip whitelist�� �����迡 ���� (�������̴ϱ�..)
    - connect���� user ����
4. Choose a connection method
    - Connect your application ����
    - "mongodb+srv://chicken:<password>@cluster0.3vo5a.mongodb.net/<dbname>?retryWrites=true&w=majority"�� ��� ������ ��й�ȣ�� ���ļ� index.js���� mongodb ������ �����Ѵ�.

5. ���� ����

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
        trim: true, // ���ڿ� �� �Էµ� ���� ����
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
    // ��ȿ�� ����
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

### ��ġ

```shell
$ npm install body-parser --save
npm WARN boiler-plate@1.0.0 No repository field.

+ body-parser@1.19.0
updated 1 package and audited 82 packages in 1.854s

2 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

### Register Route �����

```javascript
const express = require('express')
const app = express()
const port = 3000

// [body-parser]
const bodyParser = require('body-parser');
// [model]
const { User } = require('./models/User');

// [body-parser] application/x-www-form-urlencoded ������ �����͸� �м��ؼ� ������ �� �ְ� ����
app.use(bodyParser.urlencoded({extended: true}));
// [body-parser] application/json ������ �����͸� �м��ؼ� ������ �� �ְ� ����
app.use(bodyParser.json());

// [mongoose]
var mkey = process.env.mkey
const mongoose = require('mongoose')
// [mongoose] mongodb ����
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

// [route] ȸ������
app.post('/register', (req, res) => {
    // ȸ������ ������ DB�� �Է�

    const user = new User(req.body) // body-parser ����
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

"http://localhost:3000/register"�� �ùٸ� ȸ������ ������ ��û�Ǵ� ��� "{success : true}"�� ����޴´�.

ȸ������ ���� ����
```json
{
    "name": "chicken",
    "email": "chicken@gmail.com",
    "password": "1234567"
}
```
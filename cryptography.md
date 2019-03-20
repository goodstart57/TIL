# 암호화

데이터, 메세지의 무결성 검정시

데이터 전송시 보안

## 종류

SHA-1

SHA-256

 머클트리





in youtube

khan academy rsa





md5는 너무 약해져서 쓰면 X



SHA-256

code + salt를 encrypt

```python
import hashlib

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print(sha_signature)
```


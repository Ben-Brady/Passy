from Crypto.Cipher import AES
from hashlib import sha512,sha256
from secrets import token_bytes

VersionNumbers=["0.0.1"]
def Encrypt(Password,Salt,Version,Attributes):
    if Version == VersionNumbers[-1]:
        Salt = str(token_bytes(64))
        return [sha256((Password+Salt).encode('utf-8')).hexdigest(),Salt,"0.0.1",Attributes]
    else:
        return 'fail'
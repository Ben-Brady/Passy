#import argon2
from hashlib import sha256
from secrets import token_bytes,compare_digest

def SHA256(Input: str) -> str:
    return sha256((Input).encode('utf-8')).hexdigest()

def Encrypt1(Username:str,Password:str) -> tuple:
    Salt = token_bytes(64).hex()#Generate and store the salt
    User = SHA256(Username)     #Hash the Username
    Pass = SHA256(Password+Salt)#
    return (User,[Pass,Salt])

def Check1(Username:str,Password:str,UserDict:dict) -> bool:
    Name = SHA256(Username)
    try:
        CorrectPass,Salt = UserDict[Name][0],UserDict[Name][1]
    except KeyError:
        CorrectPass,Salt = "","6add8f88e6dbd7b4356fa82a788950f4f4caf3c655d974800a0ffcf929d98e0da2e903ea541f7bf14faecb2470f072e7497e2b6c2033b73e969e8705d4b37aea"
    InputPass = SHA256(Password+Salt)
    return compare_digest(InputPass,CorrectPass)

def Encrypt2(Username:str,Password:str) -> tuple:
    Salt = token_bytes(64).hex()# Generate and store the salt
    User = SHA256(Username)     # Hash the Username
    Pass = SHA256(Password+Salt)
    return (User,[Pass,Salt])

def Check2(Username:str,Password:str,UserDict:dict) -> bool:
    Name = SHA256(Username)
    try:
        CorrectPass,Salt = UserDict[Name][0],UserDict[Name][1]
    except KeyError:
        CorrectPass,Salt = "","6add8f88e6dbd7b4356fa82a788950f4f4caf3c655d974800a0ffcf929d98e0da2e903ea541f7bf14faecb2470f072e7497e2b6c2033b73e969e8705d4b37aea"

    for x in range(64):#For 64 ascii characters
        InputPass = SHA256(Password+Salt+chr(32+x))#Crate a hash for
        if compare_digest(InputPass,CorrectPass):
            return True
    return False

Encrypt={
'0.0.1' : Encrypt1,
'0.0.2' : Encrypt2,
}

Check={
'0.0.1' : Check1,
'0.0.2' : Check2,
}
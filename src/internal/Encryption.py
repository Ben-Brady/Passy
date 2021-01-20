from hashlib import sha256
from secrets import token_bytes,compare_digest


def SHA256(Input):
    """Shortcut ot the SHA256 Hash"""
    return sha256((Input).encode('utf-8')).hexdigest()

def Encrypt1(Username,Password):
    Salt = token_bytes(64).hex()#Generate and store the salt
    User = SHA256(Username)
    Pass = SHA256(Password+Salt)
    
    return (User,[Pass,Salt])

def Check1(Username,Password,UserDict):
    #The values are still comapred if there is a key error
    #to help reduce the liekliness of a timing based attack
    #!Timing attack
    Name = SHA256(Username)
    
    try:
        CorrectPass,Salt = UserDict[Name][0],UserDict[Name][1]
    except KeyError:
        CorrectPass,Salt = "","6add8f88e6dbd7b4356fa82a788950f4f4caf3c655d974800a0ffcf929d98e0da2e903ea541f7bf14faecb2470f072e7497e2b6c2033b73e969e8705d4b37aea"
    
    InputPass = SHA256(Password+Salt)
    return compare_digest(InputPass,CorrectPass)

Encrypt={
'0.0.1' : Encrypt1,
}

Check={
'0.0.1' : Check1,
}
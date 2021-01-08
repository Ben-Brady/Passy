from pathlib import Path
from json import load as jload, dump as jdump, JSONDecodeError
from Crypto.Cipher import AES
from hashlib import sha512,sha256
from secrets import token_bytes, compare_digest
from internal import AccountMigration as internal

class Userbase:
    def __init__ (self):
        self.Version = "0.0.1"
        self.UserDict= {}
    def ___lt__ (self,other):# <
        pass
    def ___le__ (self,other): #<=
        pass
    def ___eq__ (self,other): #==
        return self.UserDict == other.UserDict
    def ___ne__ (self,other): #=!
        pass
    def ___gt__ (self,other): #>
        pass
    def ___ge__ (self,other): #>=
        pass
    
    def __add__ (self,other): #Combining 2 dictionaries
        temp = {}
        for key in other.UserDict: 
            if not(key in self.UserDict):
                temp[key] = other.UserDict[key]
            else:
                temp[key] = self.UserDict[key]
        return temp
    
    def __delitem__ (self,key):
        del(self.UserDict[sha256(key.encode('utf-8')).hexdigest()])
    
    def __len__ (self):
        return (len(self.UserDict))
    
    def __repr__ (self):
        return str(self.UserDict)

    def __hash__ (self):
        hash(self.UserDict)
        
    def check(self,Username,Password):
        #The values are still comapred if there is a key error
        #to help reduce the liekliness of a timing based attack
        #this needs to be fully fixed though.
        #!Timing attack
        Name = sha256(Username.encode('utf-8')).hexdigest()

        try:
            Salt    = self.UserDict[Name][1]
            PassHash= self.UserDict[Name][0]
        
        except KeyError:
            Salt    = 'aa260f7f4bd268f3961b0f2eead9265dfeaba70a306a059ea26640765f323071'
            PassHash= 'da61d266f9038bb06af2c372e68d16bc27d1fbaf1c7fe18c03e899e5cd382bbd'
        
        Pass = sha256((Password+Salt).encode('utf-8')).hexdigest()

        return compare_digest(PassHash,Pass)

    def add(self,Username,Password,Attributes=dict({})):
        Username=str(Username)
        Password=str(Password)
        if type(Attributes) != dict:raise TypeError(f"Used {type(Attributes)} instead of dict")
        
        User = sha256(Username.encode('utf-8')).hexdigest()
        
        try:
            self.UserDict[User]
        except KeyError:pass
        
        Salt = str(token_bytes(64))
        Output = internal.Encrypt(Password,Salt,self.Version,Attributes)
        
        self.UserDict[User] = Output
    
        
    def load(self,File):
        #if File isn't a path object
        if type(File) != type(Path()):   raise TypeError
        #If file doesn't exist, riase a FileNotFoundError
        if Path(File).exists() == False: raise FileNotFoundError
    
        with open(File, 'r') as f:
            self.UserDict = jload(f)

    def save(self,File):
        #if File isn't a path object
        if type(File) != type(Path()): raise TypeError
    
        with open(File, 'w') as f:
            jdump(self.UserDict, f)
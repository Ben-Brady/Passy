import atexit
from hashlib import sha512,sha256
from secrets import token_bytes, compare_digest
from json import load, dump, JSONDecodeError
from Crypto.Cipher import AES

UserDict = {}

def Load(FileName,*FilePath):
    """
    Loads\n
    Optional parameter for file name and file path\n
    Defualt: Credentials.json
    """
    with open(FileName, 'r') as f:
        UserDict = load(f)

def Save(FileName,*FilePath):
    """
    Saves the current users list to json\n
    Optional parameter for file name and file path
    """
    with open(FileName, 'w') as f:
        dump(UserDict, f)
    return True
    #Check success
# ------------- Fix Later ------------ #


def AddUser(Username,Password,*Attributes):
    """
    Adds an account to the internal user dictionary\n
    returns a bool stating sucess
    """
    if (Attributes in locals()) == False:
        Attributes = None
    User = sha512(Username.encode('utf-8')).hexdigest()
    Salt = str(token_bytes(64))
    UserDict[User] = [sha256((Password+Salt).encode('utf-8')).hexdigest(),Salt,Attributes]

def CheckCreds(Username,Password):
    """
    Returns a bool for if the credentials are correct
    """
    #The values are still comapred if there is a key error
    #to help reduce the liekliness of a timing based attack
    #this needs to be fully fixed though.
    #BUG - Timing attack possible here
    Name    = sha512(Username.encode('utf-8')).hexdigest()
    try:
        Salt    = UserDict[Name][1]
        CPass    = UserDict[Name][0]
    except KeyError:
        Salt    = 'aa260f7f4bd268f3961b0f2eead9265dfeaba70a306a059ea26640765f323071'
        CPass   = 'da61d266f9038bb06af2c372e68d16bc27d1fbaf1c7fe18c03e899e5cd382bbd'
    Pass    = sha256((Pass+Salt).encode('utf-8')).hexdigest()
    
    if compare_digest(CPass,Pass):return True
    else:return False


if __name__ == "__main__":
    print (f"Load Success: {Load('credentails.json')}")
    print(UserDict)
    print (f"Save Success: {Save('credentails.json')}")
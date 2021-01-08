from Passy import Userbase
from pathlib import Path
test = Userbase()
def test_LoadNormalStringArg():
    try:
        CompareFiles('users.json',test.load('users.json'))
    except TypeError:
        return
    assert True == False
def  test_LoadNormalPath():
    try:
        test.load(Path(r'C:\Users\benbr\OneDrive\Scripts\Python\Passy\pytest\users.json'))
    except:
        assert False
def  test_LoadNormalFakeFile():
    try:
        test.load(Path(r'C:\Users\benbr\OneDrive\Scripts\Python\Passy\pytest\FakeFile.json'))
    except FileNotFoundError:
        return
    assert False
def CompareFiles(FileName,UserDict):
    with open(FileName, 'r') as f:
        if f == UserDict:   f.close();return True#If the saved file is identical
        else:               f.close();return False#to the stored one return True
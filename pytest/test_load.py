from passy import Database
from pathlib import Path
test = Database()
def test_LoadNormalStringArg():
    try:
        CompareFiles('users.json',test.load('users.json'))
    except TypeError:
        return
    assert True == False
def  test_LoadNormalPath():
    try:
        test.load(Path(Path.cwd(),r'pytest\TestFiles\test1.json'))
    except:
        assert False
def  test_LoadNormalFakeFile():
    try:
        test.load(Path(Path.cwd(),r'pytest\TestFiles\fakefile.json'))
    except FileNotFoundError:
        return
    assert False
def CompareFiles(FileName,UserDict):
    with open(FileName, 'r') as f:
        if f == UserDict:   f.close();return True#If the saved file is identical
        else:               f.close();return False#to the stored one return True
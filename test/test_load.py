from passy import *
from pathlib import Path
test = Database()

def test_LoadNormalStringArg():
    try:
        test.load(r'C:\Users\benbr\OneDrive\PDocuments\Scripts\Python\Passy\test\Test_Data\test1.json')
    except TypeError:
        pass

def test_LoadNormalPath():
    test.load(Path(Path.cwd(),r'test\Test_Data\test1.json'))

def test_LoadNormalFakeFile():
    try:
        test.load(Path(Path.cwd(),r'test\Test_Data\fakefile.json'))
    except FileNotFoundError:
        return
    assert False
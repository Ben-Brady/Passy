from passy import Database
from pathlib import Path
test1,test1d,test2      = Database(),Database(),Database()
test1.load  (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test1d.load (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test2.load  (Path(Path.cwd(),r'test/Test_Data/test2.json'))

def test_Init():
    assert type(test1) == Database
    assert len(test1.Version) > 0

def test_InitRepeat():
    test=Database()
    test=Database()

def test_Len():
    assert len(test1) == 2

def test_EqualPass():
    assert test1 == test1

def test_EqualFail():
    assert (not(test1 == test2))

def test_NotEqual():
    assert test1 != test2

def test_NotEqualFail():
    assert (not(test1 != test1d))

def test_LessThan():
    assert test1 < test2

def test_LessEqual():
    assert test1 <= test2

def test_GreateThan():
    assert test2 > test1

def test_LessEqual():
    assert test2 >= test1
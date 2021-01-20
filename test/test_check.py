from passy import Database
from pathlib import Path
test1,test1d,test2      = Database(),Database(),Database()
test1.load  (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test1d.load (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test2.load  (Path(Path.cwd(),r'test/Test_Data/test2.json'))

def test_CheckSuccessNormalUser():
    assert test1.check ('test1','pass1')
def test_CheckFailUser():
    assert not(test1.check ('Fail','pass1'))
def test_CheckFailPass():
    assert not(test1.check ('test1','Fail'))
def test_CheckFailBoth():
    assert not(test1.check ('Fail','Fail'))
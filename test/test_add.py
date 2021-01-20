from passy import Database
from pathlib import Path
test1,test1d,test2      = Database(),Database(),Database()
test1.load  (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test1d.load (Path(Path.cwd(),r'test/Test_Data/test1.json'))
test2.load  (Path(Path.cwd(),r'test/Test_Data/test2.json'))

def test_AddNormal():
    assert test1.add('Username','pass')
    assert test1 != test1d

def test_AddKwargs():
    assert test1.add      ('Return','pass',admin=True,key="Test")
    assert test1 != test1d

def test_AddDuplicate():
    assert test1.add      ('1','1')
    assert not(test1.add  ('1','2'))

def test_AddCheck():
    test2.add             ('AddTest','pass')
    assert     test2.check('AddTest','pass')
    assert not(test2.check('AddTest','Fail'))
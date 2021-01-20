import os
from pathlib import Path
from passy import Database

def test_Reset():
    test=Database()
    os.remove(Path(Path.cwd(),r'test/Test_Data/test1.json'))
    os.remove(Path(Path.cwd(),r'test/Test_Data/test2.json'))
    test.add("test1","pass1")
    test.add("test2","pass2")
    test.save(Path(Path.cwd(),r'test/Test_Data/test1.json'))
    test.add("test3","pass3")
    test.save(Path(Path.cwd(),r'test/Test_Data/test2.json'))
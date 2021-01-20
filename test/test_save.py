from passy import *
from pathlib import Path
from json import load as jload
import os
test = Database()

def test_SaveNormal():
    test.save   (Path(Path.cwd(),r'test\Test_Data\output.json'))
    os.remove   (Path(Path.cwd(),r'test\Test_Data\output.json'))

def test_SaveString():
    try:
        (test.save(r'C:\Users\benbr\OneDrive\PDocuments\Scripts\Python\Passy\test\Test_Data\test1.json'))
    except TypeError:
        pass
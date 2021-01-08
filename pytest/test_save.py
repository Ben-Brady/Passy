from passy import Database
from pathlib import Path
from json import load as jload
import os
test = Database()
def test_SaveNonPathObject():
    try:
        test.save('users.json')
    except TypeError:
        return
    assert False
def test_SaveNormal():
    test.save   (Path(Path.cwd(),r'pytest\TestFiles\output.json'))
    os.remove   (Path(Path.cwd(),r'pytest\TestFiles\output.json'))

test_SaveNormal()
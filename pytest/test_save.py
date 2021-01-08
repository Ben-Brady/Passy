from Passy import Userbase
from pathlib import Path
from json import load as jload
test = Userbase()
def test_SaveNonPathObject():
    try:
        test.save('users.json')
    except TypeError:
        return
    assert False
def test_SaveNormal():
    try:
        test.save(Path(r'C:\Users\benbr\OneDrive\Scripts\Python\Passy\pytest\users.json'))
    except:
        assert False
    return
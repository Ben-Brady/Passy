from passy import Database
test = Database()
def test_CheckSuccessNormalUser():
    test.add   ('abcdefghijklmnopqrstuvwxyz','password')
    assert True == test.check ('abcdefghijklmnopqrstuvwxyz','password')
def test_CheckFailWrongUser():
    test.add   ('User','password')
    assert False == test.check ('Fail','password')
def test_CheckFailWrongPass():
    test.add   ('User','password')
    assert False == test.check ('User','Fail')
def test_CheckFailWrongBoth():
    test.add   ('User','password')
    assert False == test.check ('fail','fail')
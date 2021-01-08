import Passy
test = Passy.Userbase()

def test_AddNormalUser():
    test.add   ('TestUser','password')
    assert True == test.check ('TestUser','password')
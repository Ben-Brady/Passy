import passy
test = passy.Database()

def test_AddNormalUser():
    test.add   ('TestUser','password')
    assert True == test.check ('TestUser','password')
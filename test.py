from passy import Auth


auth = Auth.create("password")
assert auth.login("password")
assert not auth.login("password2")

data = auth.dumps()
print(data)
auth = auth.loads(data)
assert auth.login("password")

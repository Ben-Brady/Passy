from passy import Auth
from pytest import fixture

@fixture
def example_account():
    return Auth("password")


def test_create_account():
    auth = Auth.create("password")


def test_dumps(example_account: Auth):
    auth_str = example_account.dumps()
    assert isinstance(auth_str, str)
    assert len(auth_str) > 0


def test_dumps_with_otp():
    auth = Auth.create("password")
    auth.add_2fa()
    auth_str = auth.dumps()
    assert isinstance(auth_str, str)
    assert len(auth_str) > 0


def test_loads(example_account: Auth):
    Auth("password")
    as
    ...

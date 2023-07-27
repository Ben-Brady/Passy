from passy import Auth
from pytest import fixture


@fixture
def ExampleAccount():
    return Auth("password")


def test_create_account():
    auth = Auth.create("password")

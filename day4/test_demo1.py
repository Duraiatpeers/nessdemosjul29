import pytest

@pytest.fixture(scope="module")
def init():
    print("Before the Module")
    yield
    print("After the Module")

def test_add(init):
    assert True

def test_sub():
    assert True


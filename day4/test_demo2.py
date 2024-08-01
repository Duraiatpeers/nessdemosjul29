
import pytest

def getdatafromexcel():
    data = []

    data.append(('sam', 'welcome'))
    data.append(('admin', 'admin'))
    return data

@pytest.mark.parametrize("username,password",getdatafromexcel())
def test_add(username,password):
    print(username)
    print(password)

import pytest

@pytest.fixture
def generate_data():
    username = 'admin1234'
    pwd = 'admin1234'
    return username, pwd

def test_check_pwd(generate_data):
    username, pwd = generate_data
    if 8 <= len(pwd) <= 16:
        assert True
    else:
        assert False
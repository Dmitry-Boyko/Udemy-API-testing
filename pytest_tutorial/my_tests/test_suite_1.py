import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
def test_login_page_valid_user():
    print("Login with valis password")
    print("Function: aaaa")
@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbb")

    # assert 1==2, 'One is not two'
import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]

@pytest.fixture(scope = 'module')
def my_setup():
    print("")
    print(">>>> my setup <<<")

    return {'id':20, 'name': 'Adam'}

@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print("Login with valis password")
    print("Function: aaaa")
    print("Name: {}".format(my_setup.get('name')))
    # import pdb; pdb.set_trace()


@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print("Login with wrong password")
    print("Function: bbbb")

# run: pytest -m be -s

# see results:
# my_tests\test_suite_1_with_setup.py
# >>>> my setup <<<
# Login with valis password
# Function: aaaa
# Name: Adam
# .Login with wrong password
# Function: bbbb
# .

# crate report: pytest -m be -s --html=report.html
# or pytest -m be -s --html=report.html --css=highcontrast.css --css=accessible.css
# https://pytest-html.readthedocs.io/en/latest/user_guide.html#enhancing-reports


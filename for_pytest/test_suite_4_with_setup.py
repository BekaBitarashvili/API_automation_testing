import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]


@pytest.fixture(scope="module")
def my_setup():
    print("")
    print(">>> My_Setup <<<")


@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print("")
    print("test_login_page_valid_user")
    print("Function: 12345678")


@pytest.mark.regression
def test_login_page_invalid_user(my_setup):
    print("test_login_page_invalid_user")
    print("Function: 00000000")

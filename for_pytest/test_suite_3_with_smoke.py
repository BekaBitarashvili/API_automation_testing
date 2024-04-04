import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
def test_login_page_valid_user():
    print("test_login_page_valid_user")
    print("Function: 12345678")


@pytest.mark.regression
def test_login_page_invalid_user():
    print("test_login_page_invalid_user")
    print("Function: 00000000")

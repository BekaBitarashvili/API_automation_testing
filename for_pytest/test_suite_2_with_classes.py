import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
class TestCheckout(object):
    def test_checkout(self):
        print("TestCheckout.test_checkout")
        print("Function: 12345678")

    def test_checkout_invalid(self):
        print("TestCheckout.test_checkout_invalid")
        print("Function: 00000000")

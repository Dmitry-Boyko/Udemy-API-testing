import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
class TestCheckout(object):
    def test_checkout_as_guest(self):
        print("checkout as a guest")
        print("Class: 111")

    def test_checkout_with_exising_usert(self):
        print("checkout with existing user")
        print("Class: 222")
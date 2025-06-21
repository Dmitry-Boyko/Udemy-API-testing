# test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://example.com/login")
    driver.find_element(By.NAME, "username").send_keys("valid_user")
    driver.find_element(By.NAME, "password").send_keys("valid_password")
    driver.find_element(By.ID, "login-button").click()

    # Example assertion: check for a logout button or dashboard element
    assert driver.find_element(By.ID, "logout-button").is_displayed()
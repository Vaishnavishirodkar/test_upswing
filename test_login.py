import pytest
from selenium import webdriver
from test import BASE_URL
from data import valid_credentials, invalid_credentials
import time
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

# verification for successful login
def test_login_positive(setup):
    driver = setup
    click_element=driver.find_element( By.ID, "login2").click()
    time.sleep(3)
    send_keys_to_element1=driver.find_element( By.ID, "loginusername")
    send_keys_to_element1.send_keys(valid_credentials["username"])
    send_keys_to_element2=driver.find_element( By.ID, "loginpassword")
    send_keys_to_element2.send_keys(valid_credentials["password"])
    login_submit=driver.find_element( By.XPATH, "//button[text()='Log in']").click()

# verification for error message
def test_login_negative(setup):
    driver = setup
    click_element=driver.find_element( By.ID, "login2").click()
    send_keys_to_element=driver.find_element( By.ID, "loginusername")
    send_keys_to_element.send_keys(invalid_credentials["username"])
    send_keys_to_element=driver.find_element( By.ID, "loginpassword")
    send_keys_to_element.send_keys(invalid_credentials["password"])
    login_element=driver.find_element( By.XPATH, "//button[text()='Log in']").click()

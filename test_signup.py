import pytest
from selenium import webdriver
from test import BASE_URL
import time
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
# verification for successful signup
def test_signup_positive(setup):
    driver = setup
    click_element=driver.find_element( By.ID, "signin2").click()
    time.sleep(3)
    send_keys_to_element=driver.find_element(By.ID, "sign-username")
    send_keys_to_element.send_keys("test_vaishnavi2")
    time.sleep(3)
    element=driver.find_element( By.ID, "sign-password")
    element.send_keys("1")
    submit_element=driver.find_element( By.XPATH, "//button[text()='Sign up']").click()

# verification for error message
def test_signup_negative(setup):
    driver = setup
    click_element=driver.find_element( By.ID, "signin2").click()
    time.sleep(3)
    send_keys_element1=driver.find_element( By.ID, "sign-username")
    send_keys_element1.send_keys("")
    send_keys_element2=driver.find_element( By.ID, "sign-password")
    send_keys_element2.send_keys("")
    submit_element2=driver.find_element( By.XPATH, "//button[text()='Sign up']").click()
    

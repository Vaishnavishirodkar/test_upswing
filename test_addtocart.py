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

def test_add_product_to_cart(setup):
    driver = setup
    click_element=driver.find_elements( By.LINK_TEXT, "Samsung galaxy s6").click()
    click_element1=driver.find_elements( By.XPATH, "//a[text()='Next']").click()
    products = driver.find_elements(By.CLASS_NAME, "hrefch")
    products[-1].click()
    click=driver.find_elements( By.XPATH, "//a[text()='Add to cart']").click()


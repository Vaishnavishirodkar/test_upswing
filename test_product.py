import pytest
from selenium import webdriver
from test import BASE_URL
from object import find_element, click_element
import time
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_product_display(setup):
    driver = setup
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    assert len(products) > 0

def test_category_navigation(setup):
    driver = setup
    click_element=driver.find_elements( By.LINK_TEXT, "Samsung galaxy s6")
    click_element.click()
    category_title = find_element(driver, By.CLASS_NAME, "card-img-top img-fluid")
    assert category_title.is_displayed()

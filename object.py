from selenium.webdriver.common.by import By

def find_element(driver, by, value):
    return driver.find_element(by, value)

def click_element(driver, by, value):
    element = find_element(driver, by, value)
    element.click()

def send_keys_to_element(driver, by, value, keys):
    element = find_element(driver, by, value)
    element.clear()
    element.send_keys(keys)
from selenium import webdriver
from tests.login import LoginTests

login_tests = LoginTests()

def open_firefox():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    return driver

driver = open_firefox()

try:
    login_tests.t01_successful_login(driver)
finally:
    driver.quit()
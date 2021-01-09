from utils.driver_manager import DriverManager
from selenium import webdriver
from tests.login import LoginTests

driver_manager = DriverManager('Firefox')
login_tests = LoginTests()

try:
    login_tests.t01_successful_login(driver_manager.driver)
    login_tests.t02_unsuccessful_login(driver_manager.driver)
finally:
    driver_manager.close_browser()
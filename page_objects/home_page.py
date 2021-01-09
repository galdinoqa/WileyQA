from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.login_modal import LoginModal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class HomePage():
    
    img_wiley_logo_header = (By.CSS_SELECTOR, '.brand-logo--desktop')
    btn_enter = (By.CSS_SELECTOR, '.js-login-member-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def given_that_i_am_on_home_page(self):
        self.driver.get('https://teamshift-qa.crossknowledge.com/')
        self.then_i_see_the_home_page()

    def when_i_click_on_enter_button(self):
        self.driver.find_element(*self.btn_enter).click()
        return LoginModal(self.driver)

    def then_i_see_the_home_page(self):
        self.wait.until(visibility_of_element_located(self.btn_enter))
        self.driver.find_element(*self.img_wiley_logo_header)
        self.driver.find_element(*self.btn_enter)
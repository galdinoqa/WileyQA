from page_objects.login_modal import LoginModal
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    
    img_wiley_logo_header = (By.CSS_SELECTOR, '.brand-logo--desktop')
    btn_enter = (By.CSS_SELECTOR, '.js-login-member-button')

    def __init__(self, driver):
        self.driver = driver

    def given_that_i_am_on_home_page(self):
        self.driver.get('https://teamshift-qa.crossknowledge.com/')
        self.driver.find_element(*self.img_wiley_logo_header)
        self.driver.find_element(*self.btn_enter)

    def when_i_click_on_enter_button(self):
        self.driver.find_element(*self.btn_enter).click()
        return LoginModal(self.driver)
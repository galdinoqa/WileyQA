from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable

class MemberArea():
    
    header_menu = (By.CSS_SELECTOR, '.header__menu')
    lbl_member_name_header = (By.CSS_SELECTOR, '.header__menu-member-name')
    btn_create_team = (By.CSS_SELECTOR, '.section-no-teams__button')
    btn_logout = (By.CSS_SELECTOR, '.header-member__menu-text--logout')
    btn_accept_cookies = (By.ID, 'js-agree-cookie-policy')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def then_i_should_see_the_member_area_page(self):
        self.wait.until(visibility_of_element_located(self.header_menu))
        self.wait.until(visibility_of_element_located(self.lbl_member_name_header))
        self.wait.until(element_to_be_clickable(self.btn_create_team))
        self.wait.until(element_to_be_clickable(self.btn_accept_cookies))

    def and_my_name_should_be_on_the_page_header(self, expected_name):
        self.wait.until(visibility_of_element_located(self.lbl_member_name_header))
        member_name_obtained = self.driver.find_element(*self.lbl_member_name_header).text
        assert member_name_obtained == expected_name
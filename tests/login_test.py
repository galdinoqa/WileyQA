import pytest
from selenium import webdriver
from page_objects.home_page import HomePage
from utils.driver_manager import DriverManager
from page_objects.login_modal import LoginModal
from page_objects.member_area import MemberArea

class TestLogin:
    @classmethod
    def setup_class(self):
        dm = DriverManager('Firefox')
        self.driver = dm.driver

    @classmethod
    def teardown_class(self):
        if self.driver != None:
            self.driver.quit()
    
    def setup_method(self, method):
        current_url = self.driver.current_url
        if current_url != 'about:blank':
            self.driver.delete_all_cookies()
            self.driver.execute_script('window.localStorage.clear();')
    
    def test01_successful_login_test(self):
        home = HomePage(self.driver)
        home.given_that_i_am_on_home_page()
        login_modal = home.when_i_click_on_enter_button()
        login_modal.then_i_should_see_a_modal_asking_for_my_email()
        login_modal.when_i_fill_the_email('galdino.qa@gmail.com')
        login_modal.and_i_click_on_next_button()
        login_modal.then_i_should_see_a_field_to_enter_my_password()
        login_modal.when_i_type_the_password('WLS2020qa')
        member_area = login_modal.and_i_click_on_login_button()
        member_area.then_i_should_see_the_member_area_page()
        member_area.and_my_name_should_be_on_the_page_header('Thiago Secomandi Galdino')

    def test02_unsuccessful_login_test(self):
        home = HomePage(self.driver)
        home.given_that_i_am_on_home_page()
        login_modal = home.when_i_click_on_enter_button()
        login_modal.then_i_should_see_a_modal_asking_for_my_email()
        login_modal.when_i_fill_the_email('galdino.qa@gmail.com')
        login_modal.and_i_click_on_next_button()
        login_modal.then_i_should_see_a_field_to_enter_my_password()
        login_modal.when_i_type_the_password('SENHA')
        login_modal.and_i_click_on_login_button()
        login_modal.then_i_should_see_an_error_message()
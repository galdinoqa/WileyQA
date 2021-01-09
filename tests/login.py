from selenium import webdriver
from page_objects.home_page import HomePage
from page_objects.login_modal import LoginModal
from page_objects.member_area import MemberArea

class LoginTests():
    
    def t01_successful_login(self, driver):
        print('Starting execution of test case T01 - Successful Login.')
        home = HomePage(driver)
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
        print('Finished execution of test case T01 - Successful Login with PASSED status.')
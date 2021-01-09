from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from page_objects.member_area import MemberArea

class LoginModal():
    
    modal_login_member = (By.ID, 'js-modal-login-member')
    lbl_header_login_modal = (By.XPATH, '//h2[contains(@class,"login-header__title")]')
    lbl_text_login_modal = (By.CSS_SELECTOR, '.login-member__subtitle')
    txt_email_login = (By.ID, 'login-form__login')
    btn_cancel_login = (By.XPATH, '//div[@id="js-modal-login-member"]//button[contains(@class,"button-default--secondary")]')
    btn_next_login = (By.XPATH, '//div[@id="js-modal-login-member"]//button[@type="submit"]')
    txt_password_login = (By.ID, 'login-form__password')
    lnk_fogot_password = (By.CSS_SELECTOR, '.login-form__forgot-password')
    lnk_request_access_link = (By.CSS_SELECTOR, '.js-login-form-request')
    btn_login = (By.XPATH, '//div[@id="js-modal-login-member"]//button[@type="submit"]')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def then_i_should_see_a_modal_asking_for_my_email(self):
        self.driver.find_element(*self.modal_login_member)
        header_text = self.driver.find_element(*self.lbl_header_login_modal).text
        assert header_text == 'Faça o login no TeamSHIFT'
        subtitle_text = self.driver.find_element(*self.lbl_text_login_modal).text
        assert subtitle_text == 'Para fazer login no TeamSHIFT, insira o seu e-mail corporativo:'
        self.driver.find_element(*self.txt_email_login)
        cancel_button_text = self.driver.find_element(*self.btn_cancel_login).text
        assert cancel_button_text == 'CANCELAR'
        next_button_text = self.driver.find_element(*self.btn_next_login).text
        assert next_button_text == 'PRÓXIMO', 'Obtained: ' + next_button_text

    def when_i_fill_the_email(self, email):
        self.wait.until(visibility_of_element_located(self.txt_email_login))
        self.driver.find_element(*self.txt_email_login).send_keys(email)

    def and_i_click_on_next_button(self):
        self.wait.until(visibility_of_element_located(self.btn_next_login))
        self.driver.find_element(*self.btn_next_login).click()

    def then_i_should_see_a_field_to_enter_my_password(self):
        self.wait.until(visibility_of_element_located(self.txt_password_login))
        self.driver.find_element(*self.txt_password_login)
        self.driver.find_element(*self.lnk_fogot_password)
        self.driver.find_element(*self.lnk_request_access_link)
        login_button_text = self.driver.find_element(*self.btn_login).text
        assert login_button_text == 'LOGIN'

    def when_i_type_the_password(self, password):
        self.wait.until(visibility_of_element_located(self.txt_password_login))
        self.driver.find_element(*self.txt_password_login).send_keys(password)

    def and_i_click_on_login_button(self):
        self.wait.until(visibility_of_element_located(self.btn_login))
        self.driver.find_element(*self.btn_login).click()
        return MemberArea(self.driver)
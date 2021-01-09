from selenium import webdriver

class DriverManager():
    def __init__(self, browser_name):
        if browser_name.upper() == 'FIREFOX':
            self.driver = webdriver.Firefox()
        elif browser_name.upper() == 'CHROME':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def close_browser(self):
        if self.driver != None:
            self.driver.quit()
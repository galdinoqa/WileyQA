from selenium import webdriver

class DriverManager():
    def __init__(self, browser_name):
        if browser_name.upper() == 'FIREFOX':
            self.open_firefox()
        elif browser_name.upper() == 'CHROME':
            self.open_chrome()

    def open_firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        return self.driver

    def open_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        return self.driver

    def close_browser(self):
        if self.driver != None:
            self.driver.quit()
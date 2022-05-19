from selenium.webdriver.common.by import By

from configs import config
from pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[id="login"]')

    def do_login(self):
        user_name = config.USER_NAME
        password = config.PASSWORD
        self.send_keys(self.USER_NAME, user_name)
        self.send_keys(self.PASSWORD, password)
        self.is_present(self.LOGIN_BUTTON).click()
        self.driver.implicitly_wait(3)
        self.wait_page_loaded()

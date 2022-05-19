from config.config import LOGIN_URL
from pages.login_page import LoginPage


class TestLoginPage:
    def test_do_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.do_login()
        current_url = login_page.current_url()

        assert current_url == 'https://demoqa.com/profile'

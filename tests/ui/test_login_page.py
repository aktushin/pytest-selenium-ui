import allure
import pytest

from cfg.config import LOGIN_URL
from pages.ui.login_page import LoginPage


@pytest.mark.ui
class TestLoginPage:
    @allure.suite('Login page')
    @allure.title('Do login')
    @allure.description
    def test_do_login(self, driver):
        """Do login and assert that current page is /profile """

        login_page = LoginPage(driver)
        login_page.open(LOGIN_URL)
        login_page.do_login()
        current_url = login_page.current_url()

        assert current_url == 'https://demoqa.com/profile'

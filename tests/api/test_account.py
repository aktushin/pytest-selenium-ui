import pytest

from schemas.authorization import GenerateTokenSuccess

from pages.api.account_page import Account
from data.api_data import AuthData


@pytest.mark.api
class TestAuth:
    auth_data = AuthData()

    # Logins and passwords for tests
    valid_auth_data = auth_data.valid_auth_data
    invalid_user_name = auth_data.invalid_user_name
    invalid_pass = auth_data.invalid_pass

    invalid_auth_list = [invalid_user_name, invalid_pass]

    def test_valid_auth(self):
        """Authorization with valid login and pass"""
        url = 'https://demoqa.com/Account/v1/Authorized'
        json = self.valid_auth_data
        auth_page = Account()
        response = auth_page.auth(url=url, json=json)
        assert response.status_code == 200
        assert response.text.lower() == 'true'

    @pytest.mark.parametrize('json', invalid_auth_list)
    def test_invalid_auth(self, json):
        """Authorization with invalid login or pass"""
        url = 'https://demoqa.com/Account/v1/Authorized'
        auth_page = Account()
        response = auth_page.auth(url=url, json=json)
        assert response.status_code == 404

    def test_generate_token(self):
        url = 'https://demoqa.com/Account/v1/GenerateToken'
        auth_page = Account()
        valid_auth_data = self.valid_auth_data

        response = auth_page.auth(url=url, json=valid_auth_data)
        auth_page.validator(GenerateTokenSuccess, response.text)
        assert response.status_code == 200


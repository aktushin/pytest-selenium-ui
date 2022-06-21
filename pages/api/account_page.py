from requests import Response

from pages.api.base_api import BaseApi


class Account(BaseApi):
    valid_data = {
            "userName": "123",
            "password": "123"
        }
    invalid_username = {
            "userName": "123",
            "password": "123"
        }
    invalid_pass = {
            "userName": "123",
            "password": "123"
        }

    def auth(self) -> Response:
        url = 'https://demoqa.com/Account/v1/Authorized'
        json = {
            "userName": "123",
            "password": "123"
        }
        response = self.post(url, json=json)

        return response


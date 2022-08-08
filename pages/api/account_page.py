from requests import Response

from pages.api.base_api import BaseApi


class Account(BaseApi):

    def auth(self, url: str, json: dict) -> Response:
        response = self.post(url, json=json)

        return response


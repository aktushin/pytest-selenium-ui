import requests
from requests import Response

from cfg.config import logger


class BaseApi:

    def get(self, url: str, headers: dict = None, params=None, cookies: str = None) -> Response:
        try:
            response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
            logger.debug(f'{url=}, {headers=}, {params=}, {cookies=}, code = {response.status_code}')
        except Exception as e:
            logger.error(e)
            raise e
        return response

    def post(self, url: str, headers: dict = None, data=None, json=None, cookies: str = None) -> Response:
        response = None

        try:
            if json:
                response = requests.post(url=url, headers=headers, json=json)
                logger.debug(f'{url=}, {headers=}, {json=}, {cookies=}, code = {response.status_code}')
            elif data:
                response = requests.post(url=url, headers=headers, data=data)
                logger.debug(f'{url=}, {headers=}, {data=}, {cookies=}, code = {response.status_code}')
            else:
                logger.error('Enter json or data for request body')

            return response

        except Exception as e:
            logger.error(e)
            raise e

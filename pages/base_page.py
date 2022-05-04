import logging.config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from config.logger_config import LOGGING
from config.config import TIMEOUT


logging.config.dictConfig(LOGGING)
logger = logging.getLogger('logger')


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        logger.debug(f'Go to URL {url}')

    def is_present(self, locator):
        """An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        :param locator: used to find the element
        :return: WebElement
        """
        try:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                ec.presence_of_element_located(locator)
            )
            logger.debug(f'Element with locator {locator} was found.')
        except TimeoutException:
            msg = f'TIMEOUT EXCEPTION! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return element

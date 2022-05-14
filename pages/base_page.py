import time

import logging.config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

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
        """ An expectation for checking that an element is present on the DOM
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

    def is_visible(self, locator):
        """ An expectation for checking that an element is present on the DOM of a
        page and visible. Visibility means that the element is not only displayed
        but also has a height and width that is greater than 0.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                ec.visibility_of_element_located(locator)
            )
            logger.debug(f'Element with locator {locator} was found.')
        except TimeoutException:
            msg = f'TIMEOUT EXCEPTION! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return element

    def is_clickable(self, locator):
        """
        An Expectation for checking an element is visible and enabled such that
        you can click it.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                ec.element_to_be_clickable(locator)
            )
            logger.debug(f'Element with locator {locator} was found.')
        except TimeoutException:
            msg = f'TIMEOUT EXCEPTION! Element with locator {locator} not found. Maybe, element not clickable?'
            logger.error(msg)
            raise Exception(msg)

        return element

    def are_present(self, locator):
        """ An expectation for checking that there is at least one element present
            on a web page.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            elements = WebDriverWait(self.driver, TIMEOUT).until(
                ec.presence_of_all_elements_located(locator)
            )
            logger.debug(f'Element with locator {locator} was found.')
        except TimeoutException:
            msg = f'TIMEOUT EXCEPTION! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return elements

    def are_visible(self, locator):
        """ An expectation for checking that all elements are present on the DOM of a
        page and visible. Visibility means that the elements are not only displayed
        but also has a height and width that is greater than 0.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            elements = WebDriverWait(self.driver, TIMEOUT).until(
                ec.visibility_of_all_elements_located(locator)
            )
            logger.debug(f'Element with locator {locator} was found.')
        except TimeoutException:
            msg = f'TIMEOUT EXCEPTION! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return elements

    def go_to_element(self, element):
        self.driver.execute_script('arguments[0].ScrollIntoView;', element)

    def send_keys(self, locator, keys):
        element = self.is_clickable(locator)

        element.clear()
        element.send_keys(keys)

    def current_url(self):
        return self.driver.current_url

    def click(self, locator):
        element = self.is_clickable(locator)

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def wait_page_loaded(self):
        page_loaded = False

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)

            try:
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
            except Exception as e:
                logger.error(e)
                raise

        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

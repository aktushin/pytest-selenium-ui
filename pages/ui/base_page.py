import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver

from cfg.config import logger
from cfg.config import TIMEOUT


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str) -> None:
        self.driver.get(url)
        self.wait_page_loaded()
        logger.debug(f'Go to URL {url}')

    def is_present(self, locator: tuple[By, str]) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM
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
            msg = f'TimeoutException! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return element

    def is_visible(self, locator: tuple[By, str]) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM of a
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
            msg = f'TimeoutException! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return element

    def is_clickable(self, locator: tuple[By, str]) -> WebElement:
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
            msg = f'TimeoutException. Element with locator {locator} not found. Maybe, element is not clickable?'
            logger.error(msg)
            raise Exception(msg)

        return element

    def are_present(self, locator: tuple[By, str]) -> list[WebElement]:
        """
        An expectation for checking that there is at least one element present on a web page.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            elements = WebDriverWait(self.driver, TIMEOUT).until(
                ec.presence_of_all_elements_located(locator)
            )
            logger.debug(f'Elements with locator {locator} were found.')
        except TimeoutException:
            msg = f'TimeoutException! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return elements

    def are_visible(self, locator: tuple[By, str]) -> list[WebElement]:
        """
        An expectation for checking that all elements are present on the DOM of a
        page and visible. Visibility means that the elements are not only displayed
        but also has a height and width that is greater than 0.
        :param locator: used to find the element
        :return: WebElement
        """

        try:
            elements = WebDriverWait(self.driver, TIMEOUT).until(
                ec.visibility_of_all_elements_located(locator)
            )
            logger.debug(f'Elements with locator {locator} were found.')
        except TimeoutException:
            msg = f'TimeoutException! Element with locator {locator} not found. Check locator or increase timeout.'
            logger.error(msg)
            raise Exception(msg)

        return elements

    def scroll_to_element(self, element: WebElement) -> None:
        self.driver.execute_script('arguments[0].ScrollIntoView;', element)

    def send_keys(self, locator: tuple[By, str], keys: str) -> None:
        """
        Sends keys to current focused element. Before that clears the selected field from characters
        :param locator: used to find the element
        :param keys: keys to send
        """

        element = self.is_clickable(locator)
        element.click()
        element.clear()
        element.send_keys(keys)

    def current_url(self) -> str:
        current_url = self.driver.current_url
        logger.debug(f'Current url is {current_url}')
        return current_url

    def click(self, locator) -> None:
        element = self.is_clickable(locator)

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def right_click(self, locator) -> None:
        element = self.is_clickable(locator)

        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def double_click(self, locator) -> None:
        element = self.is_clickable(locator)

        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def open_new_tab(self, url: str = '') -> None:
        """
        Open new tab in browser and switches to it.
        :param url: url to be opened in new tab
        """

        current_tab = self.driver.current_window_handle
        current_tab_number = self.driver.window_handles.index(current_tab)
        new_tab_number = current_tab_number + 1
        self.driver.execute_script(f'''window.open("{url}", "_blank");''')
        self.switch_to_tab(new_tab_number)
        self.wait_page_loaded()
        logger.debug(f'Open new tab with number {new_tab_number}')

    def switch_to_tab(self, tab_number: int = None, first_tab: int = False,
                      next_tab: int = False, previous_tab: int = False) -> None:
        """
        Switch focus to desired tab

        :param tab_number: tab number to switch to
        :param first_tab: switch to first tab
        :param next_tab: switch to the right tab relative to the current one
        :param previous_tab: switch to the left tab relative to the current one
        """

        try:
            if first_tab:
                tab_number = 0
            if next_tab:
                current_tab = self.driver.current_window_handle
                handles_list = self.driver.window_handles
                tab_number = handles_list.index(current_tab) + 1
            if previous_tab:
                current_tab = self.driver.current_window_handle
                handles_list = self.driver.window_handles
                tab_number = handles_list.index(current_tab) - 1

            self.driver.switch_to.window(self.driver.window_handles[tab_number])
        except IndexError:
            tab_number = 0
            self.driver.switch_to.window(self.driver.window_handles[tab_number])

    def wait_page_loaded(self) -> None:
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

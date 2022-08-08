import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from cfg.config import logger


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome, firefox or edge')
    parser.addoption('--headless', action='store_true', default=False, help='Type True for activate headless mode')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def driver(request):
    driver = None
    browser_name = request.config.getoption('browser')
    headless_mode = request.config.getoption('headless')
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        if headless_mode:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        if headless_mode:
            firefox_options.add_argument('--headless')
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        # driver.maximize_window()

    elif browser_name == 'edge':
        edge_options = EdgeOptions()
        if headless_mode:
            edge_options.add_argument('--headless')
        edge_options.add_argument('--window-size=1920,1080')
        # edge_options.add_argument('--start-maximized')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

    else:
        logger.error('Unexpected browser. Supports browsers: chrome, firefox, edge')

    yield driver

    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=AttachmentType.PNG
                          )
        except Exception as e:
            logger.error(e)

    driver.quit()

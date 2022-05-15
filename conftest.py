import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--headless', action='store', default=False, help='Type True for activate headless mode')


@pytest.fixture
def driver(request):
    driver = None
    browser_name = request.config.getoption('browser')
    headless_mode = request.config.getoption('headless')

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless_mode:
            options.add_argument('--headless')
        # options.add_argument('--start-maximized')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()

    yield driver

    driver.quit()

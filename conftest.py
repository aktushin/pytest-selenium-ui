import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.driver = driver

    yield driver

    # driver.quit()

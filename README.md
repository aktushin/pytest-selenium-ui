# Introduction
This repository contains example of usage PageObject model with python + pytest.


# Files

[conftest.py](conftest.py) - contains all fixtures(driver initiation, make screenshot for failed tests) and custom flags for command line.

[pages/base_page.py](pages/base_page.py) - contains base methods for work with web elements and browser.

[pages/elements_page.py](pages/elements_page.py) - contains classes for pages in Elements block for https://demoqa.com.
Classes includes helpers methods for specific page.

[pages/login_page.py](pages/login_page.py) - contains classes for pages in Book Store Application block for https://demoqa.com.
Classes includes helpers methods for specific page.

[configs/config](configs/config.py) - contains config for all project: Timeouts, URL's, credentials from .env.

[configs/logger_config.py](configs/logger_config.py) - contains logger config.

[data/data.py](data/data.py) - contains input data for tests.

# How to run tests
You should have python 3.10 version or later.

Using a Python virtual env is recommended.

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```
   
2) ###For run tests with UI:
    ```bash
    pytest --browser [chrome, firefox or edge]
    ```
   *Example*:
     ```bash
    pytest --browser chrome
    ```

3) ###For run tests in headless mode:
    ```bash
    pytest --browser chrome --headless
    ```
4) ###For run tests in parallel:
    ```bash
    pytest --browser chrome -n <NUM>
    ```
   *Example*:
    ```bash
    pytest --browser chrome -n 3
    ```
   That command will run 3 browsers instance in parallel.

5) ###Rerun failed tests:
    ```bash
    pytest --browser chrome --reruns <NUM>
    ```
   *Example*:
    ```bash
    pytest --browser chrome --reruns 2
    ```

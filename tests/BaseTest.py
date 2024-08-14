import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    driver: WebDriver

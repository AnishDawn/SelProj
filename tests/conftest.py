import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver

from utilities import ReadConfigurations


def initialize_driver(browser: str) -> WebDriver:
    """
    Initializes the WebDriver based on the browser type.

    :param browser: The browser type (e.g., 'chrome', 'firefox', 'edge').
    :return: The initialized WebDriver.
    :raises ValueError: If an invalid browser name is provided.
    """
    if browser == "chrome":
        return webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        return webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        return webdriver.Edge(service=EdgeService())
    else:
        raise ValueError("Provide a valid browser name from this list: chrome/firefox/edge")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make the test report.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def setup_and_teardown(request):
    """
    Fixture to set up and tear down the WebDriver.
    """
    global driver
    driver = initialize_driver(ReadConfigurations.read_configuration("basic info", "browser"))
    driver.maximize_window()
    driver.get(ReadConfigurations.read_configuration("basic info", "app_url"))
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def log_on_failure(request):
    """
    Fixture to log a screenshot on test failure.
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)

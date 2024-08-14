from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver):
        """
        Initializes the BasePage class with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the web browser.
        """
        self.driver = driver

    def type_into_element(self, text: str, locator_name: str, locator_value: str) -> None:
        """
        Finds an element, clicks on it, clears any pre-existing text, and types the specified text into the element.

        :param text: The text to be typed into the element.
        :param locator_name: The type of locator to be used (e.g., 'id', 'name', 'class_name', 'link_text', 'xpath', 'css').
        :param locator_value: The value of the locator.
        """
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name: str, locator_value: str) -> None:
        """
        Finds an element and clicks on it.

        :param locator_name: The type of locator to be used.
        :param locator_value: The value of the locator.
        """
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name: str, locator_value: str) -> bool:
        """
        Checks if an element is displayed.

        :param locator_name: The type of locator to be used.
        :param locator_value: The value of the locator.
        :return: True if the element is displayed, False otherwise.
        """
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name: str, locator_value: str) -> str:
        """
        Retrieves the text from an element.

        :param locator_name: The type of locator to be used.
        :param locator_value: The value of the locator.
        :return: The text content of the element.
        """
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name: str, locator_value: str) -> WebElement:
        """
        Finds an element using the specified locator.

        :param locator_name: The type of locator to be used.
        :param locator_value: The value of the locator.
        :return: The WebElement found using the specified locator.
        :raises ValueError: If an invalid locator name is provided.
        """
        locator_name = locator_name.lower()

        locators = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }

        if locator_name not in locators:
            raise ValueError(f"Invalid locator name: {locator_name}")

        return self.driver.find_element(locators[locator_name], locator_value)

from selenium.webdriver.remote.webdriver import WebDriver

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        """
        Initializes the LoginPage class with a WebDriver instance.

        :param driver: WebDriver instance used to interact with the web browser.
        """
        super().__init__(driver)

    # Locators
    email_address_field_id = "user-name"
    password_field_id = "password"
    login_button_xpath = "//*[@id='login-button']"
    warning_message_xpath = "//*[@id='login_button_container']/div/form/div[3]/h3"

    def enter_email_address(self, email_address_text: str) -> None:
        """
        Enters the provided email address into the email address field.

        :param email_address_text: The email address to be entered.
        """
        self.type_into_element(email_address_text, "id", self.email_address_field_id)

    def enter_password(self, password_text: str) -> None:
        """
        Enters the provided password into the password field.

        :param password_text: The password to be entered.
        """
        self.type_into_element(password_text, "id", self.password_field_id)

    def click_on_login_button(self) -> None:
        """
        Clicks on the login button.
        """
        self.element_click("xpath", self.login_button_xpath)

    def login_to_application(self, email_address_text: str, password_text: str) -> None:
        """
        Logs into the application using the provided email address and password.

        :param email_address_text: The email address to be entered.
        :param password_text: The password to be entered.
        """
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        self.click_on_login_button()

    def retrieve_warning_message(self) -> str:
        """
        Retrieves the warning message displayed on the login page.

        :return: The text content of the warning message.
        """
        return self.retrieve_element_text("xpath", self.warning_message_xpath)

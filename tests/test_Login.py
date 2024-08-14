import pytest

from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

    file_path = ExcelUtils.get_file_path()
    login_test_data = ExcelUtils.get_data_from_excel(file_path, 'Sheet1')

    @pytest.mark.parametrize("email_address, password", login_test_data)
    def test_login_with_valid_credentials(self, email_address, password):
        login_page = LoginPage(self.driver)
        login_page.login_to_application(email_address, password)

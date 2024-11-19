from pages.login_page import *
import time
import pytest
@pytest.mark.usefixtures("setup")
class Test_LoginPage:
    def test_with_valid_data(self):
        login_driver=LoginPage(self.driver)
        login_driver.click_on_username("Admin")
        login_driver.click_on_password("admin123")
        login_driver.click_on_login_button()

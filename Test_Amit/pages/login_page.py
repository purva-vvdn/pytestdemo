from locators.login_locator import *

import time

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def click_on_username(self,username):
        self.driver.find_element(*click_username).send_keys(username)
        time.sleep(2)

    def click_on_password(self,password):
        self.driver.find_element(*click_password).send_keys(password)
        time.sleep(2)

    def click_on_login_button(self):
        self.driver.find_element(*click_login_button).click()
        time.sleep(2)

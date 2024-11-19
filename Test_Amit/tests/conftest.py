from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from locators.login_locator import *
import time
import pytest
@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    request.cls.driver=driver

    yield
    driver.quit()
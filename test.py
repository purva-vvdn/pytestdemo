from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
time.sleep(5)
   

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Maximize the browser window
    driver.maximize_window()
    
    driver.implicitly_wait(10)
    
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_field.send_keys("Admin")
    
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys("admin123")
    
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    if "dashboard" in driver.current_url.lower():
        print("Login successful!")
    else:
        print("Login failed.")
finally:
    driver.quit()

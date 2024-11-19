from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Maximize the browser window
    driver.maximize_window()
    
    # Wait for the page to load (use implicit wait or explicit wait instead of `time.sleep`)
    driver.implicitly_wait(10)
    
    # Locate and fill in the username field
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_field.send_keys("Admin")
    
    # Locate and fill in the password field
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys("admin123")
    
    # Submit the form by simulating pressing Enter
    password_field.send_keys(Keys.RETURN)
    
    # Wait to ensure the login action is complete
    time.sleep(5)
    
    # Optionally, verify login success
    if "dashboard" in driver.current_url.lower():
        print("Login successful!")
    else:
        print("Login failed.")
finally:
    # Close the browser
    driver.quit()

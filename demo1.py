from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up geckodriver
gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try: 
    # Open the website
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Please enter your email']" )))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']" )))
    username_field.send_keys("sysadmin")
    password_field.send_keys("12345678")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]")))
    login_button.click()
    wait.until(EC.url_changes("https://admin-demo.nopcommerce.com/admin/"))

    print("Login successful! Current URL:", driver.current_url)
except Exception as e:
    print("Error occurred:", e)
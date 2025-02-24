from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    driver.get("https://testc.fwt-logi.com/AdminArea/index.php")
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter user name']")))
    password_field = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter password']")))
    username_field.send_keys("sysadmin")
    password_field.send_keys("12345678")
    login_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
    login_button.click()
    wait.until(expected_conditions.url_changes("https://testc.fwt-logi.com/AdminArea/index.php"))
    print("Login successful! Current URL:", driver.current_url)
    
except Exception as e:
    print("Error occurred:", e)
 

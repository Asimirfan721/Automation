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
    
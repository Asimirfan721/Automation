from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.qualitextrading.com/")
    driver.maximize_window() 
    wait = WebDriverWait(driver, 10)
    australia_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Australia')]")))
    australia_button.click()
    print("✅ Clicked on 'Australia' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/australia"))
    print("✅ Navigated to Australia page")
    #CHile
    wait = WebDriverWait(driver, 10)
    australia_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Chile')]")))
    australia_button.click()
    print("✅ Clicked on 'Chile' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/chile"))
    print("✅ Navigated to Chile page")
    #dominican-republic
    wait = WebDriverWait(driver, 10)
    australia_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Dominican Republic')]")))
    australia_button.click()
    print("✅ Clicked on 'Dominican Republic' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/dominican-republic"))
    print("✅ Navigated to Dominican Republic page")
    #japan
    wait=WebDriverWait(driver,10)
    japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Japan')]")))
    japan_button.click()
    print("✅ Clicked on 'Japan' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/japan"))
    print("✅ Navigated to Japan page")
    


except Exception as e:
    print("❌ Error occurred while clicking 'Australia' button:", e)
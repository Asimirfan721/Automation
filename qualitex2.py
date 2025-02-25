from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Firefox WebDriver
gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    # Open the website
    driver.get("https://www.qualitextrading.com/")
    wait = WebDriverWait(driver, 10)

    # Wait for the Auction button to be visible and clickable
    auction_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'AUCTION')]")))

    # Scroll into view (if needed)
    driver.execute_script("arguments[0].scrollIntoView(true);", auction_button)
    time.sleep(1)  # Allow smooth scrolling

    # Click the Auction button
    auction_button.click()
    print("✅ Clicked on the 'AUCTION' button")

    # Wait for the auction page to load
    wait.until(EC.url_contains("how-to-buy-from-auction"))
    print("✅ Navigated to Auction page")

    get_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Get Started')]")))

    # Scroll into view (if needed)
    driver.execute_script("arguments[0].scrollIntoView(true);", get_button)
    time.sleep(1)  # Allow smooth scrolling

    # Click the Get Started button
    get_button.click()
    print("✅ Clicked on the 'Get Started' button")

except Exception as e:
    print("❌ Error:", e)

 

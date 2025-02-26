from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up geckodriver path
gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    # 1️⃣ Open the Website
    driver.get("https://www.qualitextrading.com/")
    wait = WebDriverWait(driver, 10)

    # 2️⃣ Click on "Australia" Button
    australia_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Australia')]")))
    australia_button.click()
    print("✅ Clicked on 'Australia' button")

    # 3️⃣ Wait for Navigation to Australia Page
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/australia"))
    print("✅ Navigated to Australia page")

    # 4️⃣ Scroll Down to Ensure Lazy Loaded Elements Are Visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")  
    time.sleep(2)  # Wait for elements to load

    # 5️⃣ Wait for the "Show More" Buttons to Appear and Click Them
    try:
        show_more_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Show More')]")))
        
        for button in show_more_buttons:
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", button)
            print("✅ Clicked a 'Show More' button")

    except Exception as e:
        print("❌ Error occurred while clicking 'Show More' buttons:", e)

finally:
    # 6️⃣ Close the Browser
    time.sleep(3)  # Pause to see results before closing
    driver.quit()
    print("✅ Browser closed")
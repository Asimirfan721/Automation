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

    # 4️⃣ Scroll Down Slowly Until Element is Found
    for _ in range(10):  # Scroll down multiple times
        driver.execute_script("window.scrollBy(0, 120);")  # Scroll in small steps
        time.sleep(1)  # Wait for elements to load

        try:
            part_button = driver.find_element(By.XPATH, "//div[contains(text(), '21-0130-667')]")
            print("✅ Found '21-0130-667' button")
            break  # Stop scrolling if found
        except:
            continue  # Keep scrolling if not found

    # 5️⃣ Click Using JavaScript (Ensures Click Works)
    driver.execute_script("arguments[0].scrollIntoView(true);", part_button)  # Ensure visibility
    time.sleep(1)  # Wait for stability
    driver.execute_script("arguments[0].click();", part_button)  # Force click
    print("✅ Clicked on '21-0130-667' button")

except Exception as e:
    print("❌ Error occurred:", e)

 
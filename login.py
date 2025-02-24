from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up geckodriver
gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    # 1️⃣ Open the Login Page
    driver.get("https://testc.fwt-logi.com/AdminArea/index.php")

    # 2️⃣ Wait until the username and password fields are visible
    wait = WebDriverWait(driver, 10)
    
    # Try selecting username and password fields with different attributes
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter user name']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter password']")))

    # 3️⃣ Enter Credentials
    username_field.send_keys("sysadmin")  # Replace with actual username
    password_field.send_keys("12345678")  # Replace with actual password

    # 4️⃣ Click the Login Button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
    login_button.click()

    # 5️⃣ Wait for login to process
    wait.until(EC.url_changes("https://testc.fwt-logi.com/AdminArea/index.php"))
    print("Login successful! Current URL:", driver.current_url)

except Exception as e:
    print("Error occurred:", e)
 

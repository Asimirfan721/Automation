from selenium import webdriver
from selenium.webdriver.common.by import By
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
    wait = WebDriverWait(driver, 10)

    # 2️⃣ Wait for Username & Password Fields
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter user name']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter password']")))

    # 3️⃣ Enter Credentials & Click Sign In
    username_field.send_keys("sysadmin")
    password_field.send_keys("12345678")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
    login_button.click()

    # 4️⃣ Wait for Successful Login
    wait.until(EC.url_to_be("https://testc.fwt-logi.com/AdminArea/dashboard.php"))
    print("✅ Login successful!")

    # 5️⃣ Check if "Information Management" button is inside an iframe
    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        print("🖼 Switched to iframe")
    except:
        print("⚠ No iframe detected, proceeding normally.")

    # 6️⃣ Click "Information Management" Button
    try:
        button_info_mgt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Information Management')]")))
        button_info_mgt.click()
    except:
        print("⚠ Normal click failed, trying JavaScript click")
        button_info_mgt = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Information Management')]")))
        driver.execute_script("arguments[0].click();", button_info_mgt)

    # 7️⃣ Switch back to default content
    driver.switch_to.default_content()

    # 8️⃣ Wait for Navigation to Information Management Page
    wait.until(EC.url_to_be("https://testc2.fwt-logi.com/AdminArea/subpages/info_mgt.php"))
    print("✅ Navigated to Information Management Page:", driver.current_url)

except Exception as e:
    print("❌ Error occurred:", e)
 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Set up geckodriver
gecko_path = "C:\\Users\\Al Habib Trade\\Desktop\\Selenium\\geckodriver-v0.35.0-win64\\geckodriver.exe"
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

# Open Google
driver.get("https://testc.fwt-logi.com/AdminArea/")

# Print the page title
print("Page Title:", driver.title)

# Keep the browser open until the user presses Enter
input("Press Enter to close the browser...")

# Close the browser
driver.quit()

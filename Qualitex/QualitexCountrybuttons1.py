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
    #Kenya
    wait=WebDriverWait(driver,10)
    japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Kenya')]")))
    japan_button.click()
    print("✅ Clicked on 'Kenya' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/kenya"))
    print("✅ Navigated to Kenya page")
    #Pakistan
    wait=WebDriverWait(driver,10)
    japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Pakistan')]")))
    japan_button.click()
    print("✅ Clicked on 'Pakistan' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/pakistan"))
    print("✅ Navigated to Pakistan page")
    #uganda
    wait=WebDriverWait(driver,10)
    japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Uganda')]")))
    japan_button.click()
    print("✅ Clicked on 'Uganda' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/uganda"))
    print("✅ Navigated to uganda page")
    #UK
    wait=WebDriverWait(driver,10)
    japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Uk')]")))
    japan_button.click()
    print("✅ Clicked on 'Uk' button")
    wait.until(EC.url_to_be("https://www.qualitextrading.com/country/uk"))
    print("✅ Navigated to Uk page")
    # Zambia
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Zambia')]")))
    # japan_button.click()
    # print("✅ Clicked on 'Zambia' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/zambia"))
    # print("✅ Navigated to Zambia page")
    # #Trinidad and Tobago
    # wait = WebDriverWait(driver, 10)
    # trinidad_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Trinidad and Tobago')]")))
    # driver.execute_script("arguments[0].scrollIntoView();", trinidad_button)
    # trinidad_button.click()
    # print("✅ Clicked on 'Trinidad and Tobago' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/trinidad-and-tobago"))
    # print("✅ Navigated to Trinidad and Tobago page")
    # #cyprus
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Cyprus')]")))
    # japan_button.click()
    # print("✅ Clicked on 'Cyprus' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/cyprus"))
    # print("✅ Navigated to Cyprus page")
    # #guyana
    # wait = WebDriverWait(driver, 10)
    # guyana_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Guyana')]")))
    # driver.execute_script("arguments[0].scrollIntoView();", guyana_button)
    # guyana_button.click()
    # print("✅ Clicked on 'Guyana' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/guyana"))
    # print("✅ Navigated to Guyana page")
    # #ireland
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Ireland')]")))
    # japan_button.click()
    # print("✅ Clicked on 'Ireland' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/ireland"))
    # print("✅ Navigated to Ireland page")
    # #mozambique
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'mozambique')]")))
    # japan_button.click()
    # print("✅ Clicked on 'mozambique' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/mozambique"))
    # print("✅ Navigated to mozambique page")
    # #namabia
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Namabia')]")))
    # japan_button.click()
    # print("✅ Clicked on 'Namabia' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/namabia"))
    # print("✅ Navigated to Namabia page")
    # #jamaica
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Jamaica')]")))
    # japan_button.click()
    # print("✅ Clicked on 'Jamaica' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/Jamaica"))
    # print("✅ Navigated to Jamaica page")
    # #mongolia
    # wait=WebDriverWait(driver,10)

    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Mongolia')]")))
    # driver.execute_script("arguments[0].scrollIntoView();", japan_button)
    # japan_button.click()
    # print("✅ Clicked on 'mongolia' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/mongolia"))
    # print("✅ Navigated to mongolia page")
    # #zimbabwe
    # wait=WebDriverWait(driver,10)
    # japan_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'zimbabwe')]")))
    # japan_button.click()
    # print("✅ Clicked on 'zimbabwe' button")
    # wait.until(EC.url_to_be("https://www.qualitextrading.com/country/zimbabwe"))
    # print("✅ Navigated to zimbabwe page")


except Exception as e:
    print("❌ Error occurred while clicking 'Australia' button:", e)
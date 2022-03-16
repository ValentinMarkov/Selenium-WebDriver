import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Some basic navigation to www.amazon.com

# Create driver instance
service = Service('C:\\Users\\Lenovo\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)
url = "https://www.amazon.com"
driver.get(url)

driver.maximize_window()

print(driver.title)

change_language_icon = driver.find_element(By.CSS_SELECTOR, "#nav-tools .icp-nav-flag")
change_language_icon.click()
time.sleep(3)

driver.quit()

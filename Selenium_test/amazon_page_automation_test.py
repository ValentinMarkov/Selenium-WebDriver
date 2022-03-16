import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Some basic navigation to www.amazon.com
driver = webdriver.Chrome(executable_path='C:\\Users\\Lenovo\\Downloads\\chromedriver.exe')

driver.get("https://www.amazon.com")
driver.maximize_window()

change_language = driver.find_element(By.CSS_SELECTOR, "#nav-tools .icp-nav-flag")
change_language.click()
time.sleep(3)

driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Some basic navigation to www.amazon.com

# Create driver instance
service = Service('C:\\Users\\ValMar\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)
url = "https://www.amazon.com"
driver.get(url)

driver.maximize_window()

search_field = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
search_field.send_keys("mouse")

search_btn = driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button')
search_btn.click()

list_of_items = driver.find_elements(By.CSS_SELECTOR, '.s-main-slot .s-result-item span.a-size-medium')

title_list = []
for item in list_of_items:
    title_list.append(item.text)

counter = 0
for mouse in title_list:
    counter += 1
    print(f'MOUSE #{counter}: {mouse}\n')

driver.quit()

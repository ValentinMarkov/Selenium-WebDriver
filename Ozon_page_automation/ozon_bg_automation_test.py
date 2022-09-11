import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

# Some basic navigation to www.amazon.com

# Create driver instance
service = Service('C:\\Users\\ValMar\\Downloads\\chromedriver.exe')
# service = Service('C:\\Users\\Lenovo\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)

url = "https://www.ozone.bg/homepage.php/"
driver.maximize_window()
driver.get(url)


def write_up_item_title(up_int):
    """Create new txt file with test result"""
    fp = open('ozon_reports/' + datetime.datetime.now().strftime("%Y-%m-%d - %H.%M.%S") + '.txt', 'w+',
              encoding="utf-8")
    count = 0
    for i in up_int:
        count += 1
        fp.write(f'{count}. {i}\n')
        fp.write('---' * 20)
        fp.write('\n')
    fp.close()


search_field = driver.find_element(By.CSS_SELECTOR, "#search")
search_field.send_keys("mouse")

search_btn = driver.find_element(By.CSS_SELECTOR, '#search_mini_form button.search-submit')
search_btn.click()

list_of_items = driver.find_elements(By.CSS_SELECTOR,
                                     '#isp_search_results_container li .isp_product_info .isp_product_title')

list_item_price = driver.find_elements(By.CSS_SELECTOR,
                                       '.isp_product_price_wrapper span.isp_product_price span.price-main')

new_results = []
for result in list_item_price:
    symbols = '\n'
    for item in symbols:
        text = result.text.replace(symbols, '')
        new_results.append(text.strip('.лв'))

print(new_results)
print(len(new_results))

"""Create dict from two list: item title and price. After txt creation write most expensive and most cheap product
 title and price"""

# count = 0
# for price in price_list:
#     count += 1
#     print(f'{count}. Item price: {price.strip("\n")}')
#     print('---' * 20)
# print('\n')

title_list = []
for item in list_of_items:
    title_list.append(item.text)

write_up_item_title(title_list)

driver.quit()

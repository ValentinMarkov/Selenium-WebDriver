import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

# Some basic navigation to https://zamunda.net/

# Create driver instance
service = Service('C:\\Users\\ValMar\\Downloads\\chromedriver.exe')
# service = Service('C:\\Users\\Lenovo\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)

url = "https://zamunda.net/"
driver.maximize_window()
driver.get(url)


def write_up_item_title(data):
    """Create new txt file with test result"""
    fp = open('zamunda_reports/' + datetime.datetime.now().strftime("%Y-%m-%d - %H.%M.%S") + '.txt', 'w+',
              encoding="utf-8")

    cnt = 1

    fp.write(f'Tot 10 Torrent from {datetime.datetime.now().strftime("%Y-%m-%d - %H.%M.%S")}\n')
    fp.write('---' * 20)
    fp.write('\n')

    for k, v in data.items():
        fp.write(f'{cnt}. {v}-{k}')
        fp.write('\n')
        cnt += 1

    fp.close()


login_btn = driver.find_element(By.CSS_SELECTOR, ".outer a[href='/login.php']")
login_btn.click()

username_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username_field.send_keys('homqk')

pass_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
pass_field.send_keys('123456')

enter_btn = username_field = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
enter_btn.click()

bananas_btn = driver.find_element(By.CSS_SELECTOR, ".outer a[href='/bananas']")
bananas_btn.click()

# Create lists for torrent titles and torrent size
list_of_titles = driver.find_elements(By.CSS_SELECTOR, '#result .notranslate b')
lst_torrent_titles = [item.text for item in list_of_titles]

lst_of_file_size = driver.find_elements(By.CSS_SELECTOR, '#result tr td:nth-child(4)')
lst_torrent_size = [item.text.strip() for item in lst_of_file_size[1:]]

dict_torrent = dict(zip(lst_torrent_size, lst_torrent_titles))

write_up_item_title(dict_torrent)
driver.quit()


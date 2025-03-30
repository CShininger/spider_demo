import json
import time
from typing import TextIO

from spider_demo.utils import create_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

browser = create_chrome_driver()
browser.get('https://login.taobao.com')

browser.implicitly_wait(10)
username_input = browser.find_element(By.CSS_SELECTOR,'#fm-login-id')
username_input.send_keys('18852933692')
password_input=browser.find_element(By.CSS_SELECTOR,'#fm-login-password')
password_input.send_keys('sxqhxd0534...')
login_button=browser.find_element(By.CSS_SELECTOR,'#login-form > div.fm-btn > button')
login_button.click()


# wait_obj = WebDriverWait(browser, 10)
# wait_obj.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.m-userinfo')))
time.sleep(20)

with open('../taobao.json', 'w') as file:  # type: TextIO
    # noinspection PyTypeChecker
    json.dump(browser.get_cookies(), file)
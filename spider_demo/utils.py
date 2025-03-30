import json
from selenium import webdriver

def create_chrome_driver(*,headless=False):  # 自动查找驱动
    options=webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    try:
        driver=webdriver.Chrome(options=options)
        driver.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {'source':'Object.defineProperty(navigator,"webdriver",{get: () => undefined})'}
        )
        return driver
    except Exception as e:
        print(f"初始化webDeiver失败：{e}")
        raise



def add_cookies(driver,cookie_file):
    with open(cookie_file,'r') as file:
        cookie_list = json.load(file)
        for cookie_dict in cookie_list:
            if cookie_dict['secure']:
               driver.add_cookie(cookie_dict)

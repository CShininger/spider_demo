from spider_demo.utils import create_chrome_driver, add_cookies

driver=create_chrome_driver()

driver.get('https://www.taobao.com')
add_cookies(driver, '../taobao.json')
driver.get('https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E6%89%8B%E6%9C%BA&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.search_manual.0&ssid=s5-e&tab=all')
input("按回车键退出...")  # 阻塞在这里，直到用户按回车
driver.quit()
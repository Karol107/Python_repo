from selenium import webdriver

import time

driver = webdriver.Chrome('C:/Drivers/chromedriver.exe')
button = 'L2AGLb'
url = 'https://google.pl'

driver.get(url)

search_box = driver.find_element_by_name('q')
driver.find_element_by_id(button).click()

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()

driver.close()

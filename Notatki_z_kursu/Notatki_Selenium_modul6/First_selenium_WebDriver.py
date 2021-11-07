#Selenium do biblioteka pythona do testow autom GUI
#biblioteka musi byc zainstalowana

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://onet.pl')
search_box = driver.find_element('q')
search_box.send_keys('selenium python')
search_box.submit()
time.sleep(5)
driver.quit()
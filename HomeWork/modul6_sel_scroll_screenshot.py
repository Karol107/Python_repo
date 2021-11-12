#napisac funkcje w selenium do scrolowania i robienia screenshotow
#Wejdz na strone https://fabrykatestow.pl przejdz pod zakladke "KURS TAPS" (poprzez klikniece, nie bezposrednio)
# Przeskroluje do miejsca, gdzie sa inf o instruktorze i zrobi screena

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium import webdriver
import  time
from selenium.webdriver.chrome.service import Service
s = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://fabrykatestow.pl')
# link = driver.find_elements_by_link_text('Kursy')
# link.click()

try:
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "#menu-item-1023")))
    element.click()
except:
    driver.quit()

# time.sleep(10)
# menu-item-1023
# napisac funkcje w selenium do scrolowania i robienia screenshotow
# Wejdz na strone https://fabrykatestow.pl przejdz pod zakladke "KURS TAPS" (poprzez klikniece, nie bezposrednio)
# Przeskroluje do miejsca, gdzie sa inf o instruktorze i zrobi screena
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import helpers.selenium_fun_wspomagajace_Karol as helper

s = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://fabrykatestow.pl')
helper.wait_for_visibility_of_element(driver,
                                                '/html/body/div/header/div/nav[1]/div/div/div/div[2]/div/div/div/ul/li[2]/a')


# time.sleep(10)
driver.quit()
#cos tam, cos tam
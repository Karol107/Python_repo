from selenium import webdriver
import helpers.selenium_fun_wspomagajace_Karol as helper
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = "https://fabrykatestow.pl"


driver = webdriver.Chrome('C:\Drivers\Chromedriver.exe')
driver.get(URL)
driver.maximize_window()
driver.find_element_by_id('menu-item-1871').click()
time.sleep(5)
helper.wait_for_visibility_of_element(driver, '//*[@id="content"]/div/div/div/section[5]/div/div/div/div[2]/div/section[1]/div/div/div[1]/div/div/div/div/div/a').click()

scrolling_element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[6]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img')
time.sleep(5)
scrolling_element.location_once_scrolled_into_view
# driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrolling_element)

# driver.execute_script('window.scrollBy(0, document.body.scrollHeight)') #skroll na koniec srtrony
driver.save_screenshot("./Zwierzu.png")
driver.quit()



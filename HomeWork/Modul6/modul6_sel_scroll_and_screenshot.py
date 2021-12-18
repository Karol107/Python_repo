from selenium import webdriver
import helpers.selenium_fun_wspomagajace_Karol as helper
import time

URL = "https://fabrykatestow.pl"
driver = webdriver.Chrome('C:\Drivers\Chromedriver.exe')
driver.get(URL)
driver.maximize_window()
driver.find_element_by_id('menu-item-1871').click()
time.sleep(2)
helper.wait_for_visibility_of_element(driver, '//*[@id="content"]/div/div/div/section[5]/div/div/div/div[2]/div/section[1]/div/div/div[1]/div/div/div/div/div/a').click()
Pokemon_capture = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[6]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img')
Pokemon_capture.location_once_scrolled_into_view
driver.save_screenshot("./Zwierzu.png")
driver.quit()



import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://www.pinterest.com/about/")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/pin-header//header/pin-grid/div/div')
search_box.click()
time.sleep(30)
print("Closing")

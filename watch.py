import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://in.pinterest.com/videos/")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/a/div/div')
search_box.click()
time.sleep(30)
print("Closing")

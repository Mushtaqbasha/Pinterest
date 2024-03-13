import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://www.pinterest.com/ideas/")
search_box = driver.find_element("xpath",'//*[@id="searchBoxContainer"]/div/div/div[2]/input')
search_box.send_keys("Wallpapers")
search_box.send_keys(Keys.ENTER)
time.sleep(30)
print("Closing")

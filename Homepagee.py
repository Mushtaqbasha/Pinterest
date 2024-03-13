import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://www.pinterest.com/")
time.sleep(20)
print("Closing")

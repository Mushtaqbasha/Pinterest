import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://www.pinterest.com/login/")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[2]/fieldset/span/div[1]/input')
search_box.send_keys("nandiniharini2003@gmail.com")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[4]/fieldset/span/div/input')
search_box.send_keys("img@123")
search_box.submit()
time.sleep(20)
print("Closing")

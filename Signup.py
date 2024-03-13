import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
print("Getting started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://www.pinterest.com/")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/button/div')
search_box.click()
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/div/input')
search_box.send_keys("canyon35@birthdaypw.com")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[4]/fieldset/span/div/input')
search_box.send_keys("Automation123")
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]/span/div/input')
search_box.send_keys("25-07-2001")
search_box.send_keys(Keys.ENTER)
time.sleep(30)

print("Closing")


from selenium import webdriver
import allure
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
@allure.severity(allure.severity_level.NORMAL)
class TestPinterest:
    @allure.severity(allure.severity_level.MINOR)
    def test_Google_Search(self):
        print("Getting started")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.pinterest.com/")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/button/div')
        search_box.click()
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/div/input')
        search_box.send_keys("kwamel01@birthdaypw.com")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[4]/fieldset/span/div/input')
        search_box.send_keys("Automation123")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]/span/div/input')
        search_box.send_keys("25-07-2001")
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        print("Closing")


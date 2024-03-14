from selenium import webdriver
import allure
import pytest
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
        self.driver.implicitly_wait(3000)
        self.driver.get("https://www.pinterest.com/login/")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[2]/fieldset/span/div[1]/input')
        search_box.send_keys("nandiniharini2003@gmail.com")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div/div[3]/form/div[4]/fieldset/span/div/input')
        search_box.send_keys("img@123")
        search_box.submit()
        time.sleep(20)
        print("Closing")

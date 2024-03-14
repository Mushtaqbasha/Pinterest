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
        self.driver.get("https://www.pinterest.com/ideas/")
        search_box = self.driver.find_element("xpath",'//*[@id="searchBoxContainer"]/div/div/div[2]/input')
        search_box.send_keys("onepiece")
        search_box.send_keys(Keys.ENTER)
        time.sleep(3    )
        print("Closing")

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
        self.driver.implicitly_wait(30)
        self.driver.get("https://in.pinterest.com/today/")
        search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/a/div/div')
        search_box.click()
        time.sleep(30)
        print("Closing")

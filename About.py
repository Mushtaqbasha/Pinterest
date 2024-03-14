from allure_commons.types import AttachmentType
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
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.implicitly_wait(30)
                self.driver.get("https://www.pinterest.com/about/")
                search_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/pin-header//header/pin-grid/div/div')
                search_box.submit()
                time.sleep(3)
                print("Closing")

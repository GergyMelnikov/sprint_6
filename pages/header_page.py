from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class Logo():
    
    yandex_logo = [By.CSS_SELECTOR, 'img[src="/assets/ya.svg"]']
    scotokat_logo = [By.CSS_SELECTOR, 'img[src="/assets/scooter.svg"]']


    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    def open_main(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')


    def click_on_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.yandex_logo)).click()


    def click_on_scotokat_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.scotokat_logo)).click()
    
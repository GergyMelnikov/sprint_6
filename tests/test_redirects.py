from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.order_page import OrderPage
from pages.header_page import Logo


class TestRedirections():
    
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)


    def test_redirect_to_main(self):
        logo_page = Logo(self.driver, self.wait)
        order_page = OrderPage(self.driver, self.wait)
        order_page.open_order('page_button')
        logo_page.click_on_scotokat_logo()

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


    def test_redirect_to_dzen(self):
        redirect_test = Logo(self.driver, self.wait)
        redirect_test.open_main()
        redirect_test.click_on_yandex_logo()
        
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])        
        current_url = self.driver.current_url
        
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Найти"]')))
        assert 'dzen' in current_url


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
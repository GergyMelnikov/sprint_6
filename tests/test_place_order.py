from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pytest

from order_page import OrderPage


class TestOrder():
   
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)


    @pytest.mark.parametrize("button, name, second, city, metro_station, color, courier_comment", [
        ("page_button", "Вася", "Петров", "Москва", "Коломенская", "both", "Comment1"),
        ("header_button", "Коля", "Иванов", "Москва", "Чистые пруды", "black", "")
        ])
    def test_place_order(self, button, name, second, city, metro_station, color, courier_comment):
        
        order = OrderPage(self.driver, self.wait)
        order.open_order(button)
        order.fill_name(name)
        order.fill_sec_name(second)
        order.fill_city(city)
        order.select_metro(metro_station)
        order.fill_phone()
        order.press_next()
        order.fill_date()
        order.select_period()
        order.select_color(color)
        order.fill_comment(courier_comment)
        order.press_place_order()
        order.confirm_order()
        
        order_placed = order.wait.until(EC.visibility_of_element_located(order.order_placed)).text
        assert 'Заказ оформлен' in order_placed


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
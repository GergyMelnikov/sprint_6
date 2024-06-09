import pytest
import allure

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.order_page import OrderPage


class TestOrder():
   
    driver = None


    @allure.title('Проверка оформления заказа')
    @allure.description('Переходим к созданию заказа, заполняем форму, формируем заказ, проверяем появление окна "Заказ оформлен".')
    @pytest.mark.parametrize("button, name, second, city, metro_station, color, courier_comment", [
        ("page_button", "Вася", "Петров", "Москва", "Коломенская", "both", "Comment1"),
        ("header_button", "Коля", "Иванов", "Москва", "Чистые пруды", "black", "")
        ])
    def test_place_order(self, driver, wait, button, name, second, city, metro_station, color, courier_comment):
        
        order = OrderPage(driver, wait)
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
        
        order_placed = order.get_text(order.order_placed)
        assert 'Заказ оформлен' in order_placed

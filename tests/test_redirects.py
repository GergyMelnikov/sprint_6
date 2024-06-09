import allure

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.order_page import OrderPage
from pages.header_page import Logo


class TestRedirections():
    
    driver = None


    @allure.title('Тест редиректа по нажатию на логотип сервиса в хедере.')
    def test_redirect_to_main(self, driver, wait):
        logo_page = Logo(driver, wait)
        order_page = OrderPage(driver, wait)
        order_page.open_order('page_button')
        logo_page.click_on_scotokat_logo()

        assert logo_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/' # Подскажи пожалуйста, как удобнее на практике делать в ассертах, на примере этого случая - сравнивать с прямым урлом или сравнивать с self.BASE_URL?


    @allure.title('Тест редиректа по нажатию на логотип яндекса в хедере.')
    def test_redirect_to_dzen(self, driver, wait):
        redirect_test = Logo(driver, wait)
        redirect_test.open_main()
        redirect_test.click_on_yandex_logo()
        
        redirect_test.switch_to_last_browser_tab()        
        
        redirect_test.wait_until_visibility(redirect_test.find_button_on_ya)
        current_url = redirect_test.get_current_url() # А в тесте норм обращаться к методу BasePage или лучше делать метод в тестируемой-пейдже, и обращаться из теста к нему?
        assert 'dzen' in current_url

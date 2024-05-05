from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


class MainPage():
    QUESTION_1 = [By.ID, 'accordion__heading-0']
    QUESTION_2 = [By.ID, 'accordion__heading-1']
    QUESTION_3 = [By.ID, 'accordion__heading-2']
    QUESTION_4 = [By.ID, 'accordion__heading-3']
    QUESTION_5 = [By.ID, 'accordion__heading-4']
    QUESTION_6 = [By.ID, 'accordion__heading-5']
    QUESTION_7 = [By.ID, 'accordion__heading-6']
    QUESTION_8 = [By.ID, 'accordion__heading-7']

    QUESTION_1_TEXT = [By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']
    QUESTION_2_TEXT = [By.XPATH, '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]']
    QUESTION_3_TEXT = [By.XPATH, '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']
    QUESTION_4_TEXT = [By.XPATH, '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']
    QUESTION_5_TEXT = [By.XPATH, '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]']
    QUESTION_6_TEXT = [By.XPATH, '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]']
    QUESTION_7_TEXT = [By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]'] 
    QUESTION_8_TEXT = [By.XPATH, '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]']
    

        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        #self.url = 'https://qa-scooter.praktikum-services.ru/'

    def open_main_page(self):
        self.driver.get(self.url)

    def scroll_to_question_8(self):
        question_8 = self.wait.until(EC.presence_of_element_located(self.QUESTION_8))
        self.driver.execute_script('arguments[0].scrollIntoView();', question_8)

    def click_on_question_1(self):
        self.driver.find_element(*self.QUESTION_1).click()

    def click_on_question_2(self):
        self.driver.find_element(*self.QUESTION_2).click()

    def click_on_question_3(self):
        self.driver.find_element(*self.QUESTION_3).click()

    def click_on_question_4(self):
        self.driver.find_element(*self.QUESTION_4).click()

    def click_on_question_5(self):
        self.driver.find_element(*self.QUESTION_5).click()

    def click_on_question_6(self):
        self.driver.find_element(*self.QUESTION_6).click()

    def click_on_question_7(self):
        self.driver.find_element(*self.QUESTION_7).click()
    
    def click_on_question_8(self):
        self.driver.find_element(*self.QUESTION_8).click()


    def get_question_text_1(self):
        return self.driver.find_element(*self.QUESTION_1_TEXT).text

    def get_question_text_2(self):
        return self.driver.find_element(*self.QUESTION_2_TEXT).text

    def get_question_text_3(self):
        return self.driver.find_element(*self.QUESTION_3_TEXT).text
    
    def get_question_text_4(self):
        return self.driver.find_element(*self.QUESTION_4_TEXT).text
    
    def get_question_text_5(self):
        return self.driver.find_element(*self.QUESTION_5_TEXT).text
    
    def get_question_text_6(self):
        return self.driver.find_element(*self.QUESTION_6_TEXT).text
    
    def get_question_text_7(self):
        return self.driver.find_element(*self.QUESTION_7_TEXT).text

    def get_question_text_8(self):
        return self.driver.find_element(*self.QUESTION_8_TEXT).text
    


class TestMainPageQuestions():
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)

    
    def test_question_text_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_1()
        received_text = my_obj.get_question_text_1()
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert received_text == expected_text

    def test_question_text_2(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_2()
        received_text = my_obj.get_question_text_2()
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert received_text == expected_text

    def test_question_text_3(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_3()
        received_text = my_obj.get_question_text_3()
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert received_text == expected_text

    def test_question_text_4(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_4()
        received_text = my_obj.get_question_text_4()
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert received_text == expected_text

    def test_question_text_5(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_5()
        received_text = my_obj.get_question_text_5()
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert received_text == expected_text

    def test_question_text_6(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_6()
        received_text = my_obj.get_question_text_6()
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert received_text == expected_text

    def test_question_text_7(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_7()
        received_text = my_obj.get_question_text_7()
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert received_text == expected_text  
    
    def test_question_text_8(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        
        my_obj = MainPage(self.driver)
        my_obj.scroll_to_question_8()
        my_obj.click_on_question_8()
        received_text = my_obj.get_question_text_8()
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert received_text == expected_text    

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

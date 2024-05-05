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

    ANSWER_1 = [By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']
    ANSWER_2 = [By.XPATH, '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]']
    ANSWER_3 = [By.XPATH, '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']
    ANSWER_4 = [By.XPATH, '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']
    ANSWER_5 = [By.XPATH, '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]']
    ANSWER_6 = [By.XPATH, '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]']
    ANSWER_7 = [By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]'] 
    ANSWER_8 = [By.XPATH, '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]']
    

        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.url = 'https://qa-scooter.praktikum-services.ru/'


    def open_main_page(self):
        self.driver.get(self.url)


    def scroll_to_question_8(self):
        question_8 = self.wait.until(EC.presence_of_element_located(self.QUESTION_8))
        self.driver.execute_script('arguments[0].scrollIntoView();', question_8)


    def click_on_question(self, question):
        element = self.wait.until(EC.element_to_be_clickable(getattr(MainPage, question)))
        element.click()


    def get_answer(self, answer):
        element = self.wait.until(EC.visibility_of_element_located(getattr(MainPage, answer)))
        return element.text



class TestMainPageQuestions():
    
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)
        

    @pytest.mark.parametrize("question, answer, expected_text", [
        ("QUESTION_1", "ANSWER_1", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("QUESTION_2", "ANSWER_2", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ("QUESTION_3", "ANSWER_3", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ("QUESTION_4", "ANSWER_4", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("QUESTION_5", "ANSWER_5", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("QUESTION_6", "ANSWER_6", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        ("QUESTION_7", "ANSWER_7", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("QUESTION_8", "ANSWER_8", "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_question_text(self, question, answer, expected_text):
        my_obj = MainPage(self.driver)
        my_obj.open_main_page()  
        my_obj.scroll_to_question_8()
        my_obj.click_on_question(question)
        received_text = my_obj.get_answer(answer)
        assert received_text == expected_text  


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

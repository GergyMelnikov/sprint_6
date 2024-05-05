from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from main_page import MainPage


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
        my_obj = MainPage(self.driver, self.wait)
        my_obj.open_main_page()  
        my_obj.scroll_to_question_8()
        my_obj.click_on_question(question)
        received_text = my_obj.get_answer(answer)
        assert received_text == expected_text  


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

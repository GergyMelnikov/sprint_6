from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class MainPage:
    # Определяем локаторы элементов вопросов и соответствующие тексты
    QUESTIONS = {
        "QUESTION_1": {"locator": By.ID, "value": "accordion__heading-0", "text": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."},
        "QUESTION_2": {"locator": By.ID, "value": "accordion__heading-1", "text": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."},
        "QUESTION_3": {"locator": By.ID, "value": "accordion__heading-2", "text": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."},
        "QUESTION_4": {"locator": By.ID, "value": "accordion__heading-3", "text": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."},
        "QUESTION_5": {"locator": By.ID, "value": "accordion__heading-4", "text": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."},
        "QUESTION_6": {"locator": By.ID, "value": "accordion__heading-5", "text": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."},
        "QUESTION_7": {"locator": By.ID, "value": "accordion__heading-6", "text": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."},
        "QUESTION_8": {"locator": By.ID, "value": "accordion__heading-7", "text": "Да, обязательно. Всем самокатов! И Москве, и Московской области."}
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_main_page(self, url):
        self.driver.get(url)

    def scroll_to_question(self, question_name):
        question = self.QUESTIONS[question_name]
        element = self.wait.until(EC.presence_of_element_located((question["locator"], question["value"])))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def get_question_text(self, question_name):
        element = self.driver.find_element(*self.QUESTIONS[question_name]["locator"], self.QUESTIONS[question_name]["value"])
        return element.text


class TestMainPageQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("question_name", ["QUESTION_1", "QUESTION_2", "QUESTION_3", "QUESTION_4", "QUESTION_5", "QUESTION_6", "QUESTION_7", "QUESTION_8"])
    def test_questions(self, question_name):
        main_page = MainPage(self.driver)
        main_page.open_main_page('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_to_question(question_name)
        received_text = main_page.get_question_text(question_name)
        expected_text = main_page.QUESTIONS[question_name]["text"]
        assert received_text == expected_text

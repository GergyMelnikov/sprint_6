import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    QUESTION_TEXT_LOCATORS = {
        "QUESTION_1": {"locator": (By.ID, 'accordion__heading-0'), "text_locator": (By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')},
        "QUESTION_2": {"locator": (By.ID, 'accordion__heading-1'), "text_locator": (By.XPATH, '//p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]')},
        "QUESTION_3": {"locator": (By.ID, 'accordion__heading-2'), "text_locator": (By.XPATH, '//p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')},
        "QUESTION_4": {"locator": (By.ID, 'accordion__heading-3'), "text_locator": (By.XPATH, '//p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')},
        "QUESTION_5": {"locator": (By.ID, 'accordion__heading-4'), "text_locator": (By.XPATH, '//p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')},
        "QUESTION_6": {"locator": (By.ID, 'accordion__heading-5'), "text_locator": (By.XPATH, '//p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]')},
        "QUESTION_7": {"locator": (By.ID, 'accordion__heading-6'), "text_locator": (By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')},
        "QUESTION_8": {"locator": (By.ID, 'accordion__heading-7'), "text_locator": (By.XPATH, '//p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]')},
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_main_page(self, url):
        self.driver.get(url)

    def scroll_to_question(self, question_locator):
        question = self.wait.until(EC.presence_of_element_located(question_locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', question)

    def click_on_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    def get_question_text(self, text_locator):
        return self.driver.find_element(*text_locator).text

class TestMainPageQuestions():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.driver, 10)

    @pytest.fixture
    def main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page('https://qa-scooter.praktikum-services.ru/')
        main_page.scroll_to_question(MainPage.QUESTION_TEXT_LOCATORS["QUESTION_8"]["locator"])
        return main_page

    @pytest.mark.parametrize("question_key, expected_text", [
        ("QUESTION_1", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("QUESTION_2", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ("QUESTION_3", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ("QUESTION_4", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("QUESTION_5", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("QUESTION_6", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        ("QUESTION_7", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("QUESTION_8", "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_question_text(self, main_page, question_key, expected_text):
        main_page.click_on_question(MainPage.QUESTION_TEXT_LOCATORS[question_key]["locator"])
        received_text = main_page.get_question_text(MainPage.QUESTION_TEXT_LOCATORS[question_key]["text_locator"])
        assert received_text == expected_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

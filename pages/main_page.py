from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
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


    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(self.BASE_URL)


    @allure.step('Прокрутить страницу к последнему вопросу')
    def scroll_to_question_8(self):
        self.scroll_into_view(self.QUESTION_8)


    @allure.step('Нажать на вопрос')
    @allure.description('Вопрос необходимо указать при вызове метода в формате "QUESTION_1"(строка), где число в конце - порядковый номер вопроса от "1" до "8"')
    def click_on_question(self, question):
        self.click(getattr(self, question))


    @allure.step('Получить ответ на вопрос')
    @allure.description('При обращении к методу указать "ANSWER_1"(строка), где число в конце - порядковый номер ответа на вопрос от "1" до "8"')
    def get_answer(self, answer):
        return self.get_text(getattr(self, answer))
    
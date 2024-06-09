from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class Logo(BasePage):
    
    yandex_logo = [By.CSS_SELECTOR, 'img[src="/assets/ya.svg"]']
    scotokat_logo = [By.CSS_SELECTOR, 'img[src="/assets/scooter.svg"]']
    
    find_button_on_ya = [By.XPATH, '//button[text()="Найти"]'] # Кнопка "Найти", на странице яндекса. К хедеру проекта эта кнопка не относится.


    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    @allure.step('Открыть главную страницу')
    def open_main(self):
        #self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.open_url(self.BASE_URL)


    @allure.step('Нажать на логотип яндекса в хедере')
    def click_on_yandex_logo(self):
        #self.wait.until(EC.element_to_be_clickable(self.yandex_logo)).click()
        self.click(self.yandex_logo)


    @allure.step('Нажать на логотип сервиса в хедере')
    def click_on_scotokat_logo(self):
        #self.wait.until(EC.element_to_be_clickable(self.scotokat_logo)).click()
        self.click(self.scotokat_logo)
    
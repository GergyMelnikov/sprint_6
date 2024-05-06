from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pytest
import allure


class OrderPage():
    
    place_order_button_header = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    place_order_button_page = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']


    name_field = [By.CSS_SELECTOR, 'input[placeholder="* Имя"]']
    second_name_field = [By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]']
    city_feild = [By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]']
    metro_station_field = [By.CSS_SELECTOR, 'div[class="select-search"]']
    phone_field = [By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[text()="Далее"]']

    date_field = [By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]']
    period_field = [By.CSS_SELECTOR, 'div[class="Dropdown-root"]']
    color_black = [By.ID, 'black']
    color_grey = [By.ID, 'grey']
    courier_comment_field = [By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]']
    place_order_button = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    
    confirm_order_creation_button = [By.XPATH, '//button[text()="Да"]']

    order_placed = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']
        
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step('Открываем главную страницу, с нее переходим к созданию заказа')
    def open_order(self, button):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.start = button
        
        if self.start == 'header_button':
            self.wait.until(EC.element_to_be_clickable(self.place_order_button_header)).click()
        elif self.start == 'page_button':
            place_order_button_page = self.wait.until(EC.presence_of_element_located(self.place_order_button_page))
            self.driver.execute_script('arguments[0].scrollIntoView();', place_order_button_page)
            self.driver.find_element(*self.place_order_button_page).click()


    @allure.step('В форме создания заказа заполняем имя')
    def fill_name(self, name):      
        self.name = name
        self.driver.find_element(*self.name_field).send_keys(name)


    @allure.step('В форме создания заказа заполняем фамилию')
    def fill_sec_name(self, second_name):     
        self.sec_name = second_name
        self.driver.find_element(*self.second_name_field).send_keys(second_name)


    @allure.step('В форме создания заказа заполняем поле "Адрес"')
    def fill_city(self, city):   
        self.city = city
        self.driver.find_element(*self.city_feild).send_keys(city)


    @allure.step('В форме создания заказа заполняем станцию метро')
    def select_metro(self, station_name):       
        self.station_name = station_name
        self.driver.find_element(*self.metro_station_field).click()

        xpath = f'.//div[text()="{station_name}"]'        
        some_station = self.driver.find_element(By.XPATH, xpath) # Не осилил через локаторы, не делать же для всего списка станиций отдельные локаторы?
        some_station.click()


    @allure.step('В форме создания заказа заполняем номер телефона случайными 11-ью цифрами')
    def fill_phone(self):
        self.number = random.randrange(70000000000, 89999999999)
        self.driver.find_element(*self.phone_field).send_keys(self.number)


    @allure.step('В форме создания заказа жмем "далее"')
    def press_next(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    @allure.step('В форме создания заказа выбираем дату')
    def fill_date(self):
        generate_date = lambda: f"{random.randint(1, 28):02d}.{random.randint(1, 12):02d}.{random.randint(2023, 2025)}"
        date = generate_date()
        self.wait.until(EC.element_to_be_clickable(self.date_field)).send_keys(date, Keys.RETURN)
        

    @allure.step('В форме создания заказа выбираем срок аренды')
    def select_period(self):
        self.wait.until(EC.element_to_be_clickable(self.period_field)).click()
        self.period = random.choice(['сутки','двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']) 
        xpath = f'//div[text()="{self.period}"]'
        select_period = self.driver.find_element(By.XPATH, xpath)
        select_period.click()


    @allure.step('В форме создания заказа выбираем цвет самоката')
    def select_color(self, color):        
        if color == 'both':
            self.color = self.wait.until(EC.element_to_be_clickable(self.color_grey)).click()
            self.color = self.wait.until(EC.element_to_be_clickable(self.color_black)).click()
        elif color == 'grey' or 'black':
            self.color = self.wait.until(EC.element_to_be_clickable(getattr(self, f"color_{color}"))).click()


    @allure.step('В форме создания заказа пишем комментарий курьеру')
    def fill_comment(self, message):
        self.message = message
        self.wait.until(EC.element_to_be_clickable(self.courier_comment_field)).send_keys(self.message)


    @allure.step('В форме создания заказа оформляем заказ')
    def press_place_order(self):
        self.wait.until(EC.element_to_be_clickable(self.place_order_button)).click()


    @allure.step('В диалоге подтверждения оформления заказа - подтверждаем')
    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_order_creation_button)).click()

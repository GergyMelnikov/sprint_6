from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import allure



class OrderPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.start = None

    
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
        


    @allure.step('Открываем главную страницу, с нее переходим к созданию заказа')
    def open_order(self, button):
        self.open_url(self.BASE_URL)
        self.start = button
        
        if self.start == 'header_button':
            self.click(self.place_order_button_header)
        elif self.start == 'page_button':
            self.scroll_into_view(self.place_order_button_page)
            self.click(self.place_order_button_page)


    @allure.step('В форме создания заказа заполняем имя')
    def fill_name(self, name):      
        self.send_keys(self.name_field, name)


    @allure.step('В форме создания заказа заполняем фамилию')
    def fill_sec_name(self, second_name):     
        self.send_keys(self.second_name_field, second_name)


    @allure.step('В форме создания заказа заполняем поле "Адрес"')
    def fill_city(self, city):   
        self.send_keys(self.city_feild, city)


    @allure.step('В форме создания заказа заполняем станцию метро')
    def select_metro(self, station_name):       
        self.click(self.metro_station_field)

        xpath = f'.//div[text()="{station_name}"]'        
        some_station = self.driver.find_element(By.XPATH, xpath) 
        self.click(some_station)


    @allure.step('В форме создания заказа заполняем номер телефона случайными 11-ью цифрами')
    def fill_phone(self):
        self.number = random.randrange(70000000000, 89999999999)
        self.send_keys(self.phone_field, str(self.number))


    @allure.step('В форме создания заказа жмем "далее"')
    def press_next(self):
        self.click(self.next_button)


    @allure.step('В форме создания заказа выбираем дату')
    def fill_date(self):
        generate_date = lambda: f"{random.randint(1, 28):02d}.{random.randint(1, 12):02d}.{random.randint(2023, 2025)}"
        date = generate_date()
        self.send_keys(self.date_field, date + Keys.RETURN)
        

    @allure.step('В форме создания заказа выбираем срок аренды')
    def select_period(self):
        self.click(self.period_field)
        self.period = random.choice(['сутки','двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']) 
        xpath = f'//div[text()="{self.period}"]'
        select_period = self.driver.find_element(By.XPATH, xpath)
        self.click(select_period)


    @allure.step('В форме создания заказа выбираем цвет самоката')
    def select_color(self, color):        
        if color == 'both':
            self.click(self.color_grey)
            self.click(self.color_black)
        elif color == 'grey' or 'black':
            self.click(getattr(self, f"color_{color}"))


    @allure.step('В форме создания заказа пишем комментарий курьеру')
    def fill_comment(self, message):
        self.send_keys(self.courier_comment_field, message)


    @allure.step('В форме создания заказа оформляем заказ')
    def press_place_order(self):
        self.click(self.place_order_button)


    @allure.step('В диалоге подтверждения оформления заказа - подтверждаем')
    def confirm_order(self):
        self.click(self.confirm_order_creation_button)
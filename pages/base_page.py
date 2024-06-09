from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def find(self, locator):
        self.driver.find_element(locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def scroll_into_view(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def get_current_url(self):
        return self.driver.current_url
    
    def open_url(self, url):
        self.driver.get(url)

    def switch_to_last_browser_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    def wait_until_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait
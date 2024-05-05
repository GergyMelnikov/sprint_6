from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class Header():
    order_button = [By.CLASS_NAME, 'Button_Button__ra12g Header_Button__28dPO']
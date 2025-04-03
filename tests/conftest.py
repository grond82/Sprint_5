import pytest
import random
from selenium import webdriver

@pytest.fixture()
def create_email():
    email = f'timofei_vasilev_20_{random.randint(100, 999)}@yandex.ru'
    return email

@pytest.fixture()
def create_password():
    password = random.randint(100000, 999999)
    return password

@pytest.fixture()
def driver_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def driver_firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
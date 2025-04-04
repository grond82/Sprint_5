from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
from tests.url import TestUrl
from tests.data import Data

class TestLogin:

    def test_login_enter_to_account_button(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.find_element(*TestLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_enter_to_my_cabinet(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.find_element(*TestLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_registration_page(self, driver_chrome):
        driver_chrome.get(TestUrl.REGISTRATION_PAGE)
        driver_chrome.find_element(*TestLocators.ENTER_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.find_element(*TestLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_password_recovery_page(self, driver_chrome):
        driver_chrome.get(TestUrl.FORGOT_PASSWORD_PAGE)
        driver_chrome.find_element(*TestLocators.ENTER_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.find_element(*TestLocators.BUTTON_ORDER).text == "Оформить заказ"
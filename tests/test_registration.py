from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
from tests.url import TestUrl

class TestRegistration:

    def test_registration_successful(self, create_email, create_password, driver_chrome):
        driver_chrome.get(TestUrl.REGISTRATION_PAGE)
        driver_chrome.find_element(*TestLocators.FIELD_NAME_ON_REGISTRATION_PAGE).send_keys('Timofei')
        driver_chrome.find_element(*TestLocators.FIELD_EMAIL_ON_REGISTRATION_PAGE).send_keys(create_email)
        driver_chrome.find_element(*TestLocators.FIELD_PASSWORD_ON_REGISTRATION_PAGE).send_keys(create_password)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver_chrome, 5).until(
            expected_conditions.text_to_be_present_in_element(TestLocators.ENTER_TEXT_ON_LOGIN_PAGE, "Вход"))
        assert '/login' in driver_chrome.current_url

    def test_registration_with_empty_name(self, create_email, create_password, driver_chrome):
        driver_chrome.get(TestUrl.REGISTRATION_PAGE)
        driver_chrome.find_element(*TestLocators.FIELD_EMAIL_ON_REGISTRATION_PAGE).send_keys(create_email)
        driver_chrome.find_element(*TestLocators.FIELD_PASSWORD_ON_REGISTRATION_PAGE).send_keys(create_password)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_PAGE).click()
        assert '/register' in driver_chrome.current_url

    def test_registration_with_wrong_email(self, create_password, driver_chrome):
        driver_chrome.get(TestUrl.REGISTRATION_PAGE)
        driver_chrome.find_element(*TestLocators.FIELD_NAME_ON_REGISTRATION_PAGE).send_keys('Timofei')
        driver_chrome.find_element(*TestLocators.FIELD_EMAIL_ON_REGISTRATION_PAGE).send_keys('testyandex.ru')
        driver_chrome.find_element(*TestLocators.FIELD_PASSWORD_ON_REGISTRATION_PAGE).send_keys(create_password)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(TestLocators.ERROR_ON_REGISTRATION_PAGE,'Такой пользователь уже существует'))
        text = driver_chrome.find_element(*TestLocators.ERROR_ON_REGISTRATION_PAGE).text
        assert text == 'Такой пользователь уже существует'

    def test_registration_with_wrong_password(self, create_email, driver_chrome):
        driver_chrome.get(TestUrl.REGISTRATION_PAGE)
        driver_chrome.find_element(*TestLocators.FIELD_NAME_ON_REGISTRATION_PAGE).send_keys('Timofei')
        driver_chrome.find_element(*TestLocators.FIELD_EMAIL_ON_REGISTRATION_PAGE).send_keys(create_email)
        driver_chrome.find_element(*TestLocators.FIELD_PASSWORD_ON_REGISTRATION_PAGE).send_keys('12345')
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(
            TestLocators.ERROR_ON_REGISTRATION_PAGE, 'Некорректный пароль'))
        text = driver_chrome.find_element(*TestLocators.ERROR_ON_REGISTRATION_PAGE).text
        assert text == 'Некорректный пароль'
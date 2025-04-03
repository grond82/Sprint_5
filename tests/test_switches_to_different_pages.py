from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
from tests.url import TestUrl

class TestSwitches:

    def test_switch_to_my_cabinet_without_login(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        assert driver_chrome.find_element(*TestLocators.ENTER_TEXT_ON_LOGIN_PAGE).text == "Вход"

    def test_switch_to_my_cabinet_with_login(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys("timofei_vasilev_20_123@yandex.ru")
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys("1qazXSW@")
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.MY_CABINET_URL))
        assert driver_chrome.current_url == TestUrl.MY_CABINET_URL

    def test_switch_from_my_cabinet_to_constructor(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys("timofei_vasilev_20_123@yandex.ru")
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys("1qazXSW@")
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_FROM_MY_CABINET_PAGE).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.current_url == TestUrl.HOMEPAGE_URL

    def test_switch_from_my_cabinet_click_on_logo(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys("timofei_vasilev_20_123@yandex.ru")
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys("1qazXSW@")
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        driver_chrome.find_element(*TestLocators.LOGO_ON_MY_CABINET_PAGE).click()
        WebDriverWait(driver_chrome, 7).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        assert driver_chrome.current_url == TestUrl.HOMEPAGE_URL
        driver_chrome.quit()
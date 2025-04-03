from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
from tests.url import TestUrl

class TestLogout:

    def test_logout_from_my_cabinet(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains('/login'))
        driver_chrome.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys("timofei_vasilev_20_123@yandex.ru")
        driver_chrome.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys("1qazXSW@")
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_to_be(TestUrl.HOMEPAGE_URL))
        driver_chrome.find_element(*TestLocators.MY_CABINET).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.text_to_be_present_in_element(TestLocators.EXIT_MY_CABINET, "Выход"))
        driver_chrome.find_element(*TestLocators.EXIT_MY_CABINET).click()
        WebDriverWait(driver_chrome, 5).until(expected_conditions.url_contains("/login"))
        assert driver_chrome.current_url == TestUrl.LOGIN_PAGE_URL
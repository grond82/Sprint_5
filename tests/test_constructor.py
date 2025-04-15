from tests.locators import TestLocators
from tests.url import TestUrl

class TestConstructor:

    def test_switch_to_filings(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).click()
        assert "tab_tab_type_current" in driver_chrome.find_element(*TestLocators.CONSTRUCTOR_FILLINGS_SELECT).get_attribute('class')

    def test_switch_to_sauces(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        assert "tab_tab_type_current" in driver_chrome.find_element(*TestLocators.CONSTRUCTOR_SAUCES_SELECT).get_attribute('class')

    def test_switch_to_buns(self, driver_chrome):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_BUNS).click()
        assert "tab_tab_type_current" in driver_chrome.find_element(*TestLocators.CONSTRUCTOR_BUNS_SELECT).get_attribute('class')
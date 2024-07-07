import allure
from config import WEB_LINK
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_6.locators.scooter_order_locators import upper_order_button, scooter_logo, status_button

class TestGoToYandexHomeScreen:

    @allure.step('Open the web page')
    def open_web_page(self, browser):
        browser.get(WEB_LINK)

    @allure.step('Click on the upper order button')
    def click_upper_order_button(self, browser):
        browser.find_element(By.XPATH, upper_order_button).click()

    @allure.step('Click on the scooter logo')
    def click_scooter_logo(self, browser):
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, scooter_logo))).click()

    @allure.step('Wait for the status button to be visible')
    def wait_for_status_button(self, browser):
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, status_button)))

    @allure.step('Verify the current URL')
    def verify_current_url(self, browser):
        assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Test Navigation to Yandex Home Screen from Order Screen')
    def test_go_to_yandex_home_screen_from_order_screen(self, browser):
        self.open_web_page(browser)
        self.click_upper_order_button(browser)
        self.click_scooter_logo(browser)
        self.wait_for_status_button(browser)
        self.verify_current_url(browser)

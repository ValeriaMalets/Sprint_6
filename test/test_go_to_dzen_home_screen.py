import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import WEB_LINK
from Sprint_6.locators.scooter_order_locators import upper_order_button, yandex_logo


@allure.feature("Navigation")
@allure.story("Navigation to Yandex from order screen")
class TestGoToYandexHomeScreen:

    @allure.title("Test navigating to Yandex home screen from order screen")
    def test_go_to_yandex_home_screen_from_order_screen(self, browser):
        self.open_website(browser)
        self.click_upper_order_button(browser)
        self.click_yandex_logo(browser)
        self.switch_to_new_window(browser)
        self.verify_new_window_title(browser)
        self.verify_new_window_url(browser)

    @allure.step("Open the website")
    def open_website(self, browser):
        browser.get(WEB_LINK)

    @allure.step("Click the upper order button")
    def click_upper_order_button(self, browser):
        browser.find_element(By.XPATH, upper_order_button).click()

    @allure.step("Click on the Yandex logo")
    def click_yandex_logo(self, browser):
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, yandex_logo))
        ).click()

    @allure.step("Switch to the new window")
    def switch_to_new_window(self, browser):
        original_window = browser.current_window_handle
        WebDriverWait(browser, 3).until(expected_conditions.new_window_is_opened)
        new_window = [window for window in browser.window_handles if window != original_window][0]
        browser.switch_to.window(new_window)

    @allure.step("Verify the new window title is 'Дзен'")
    def verify_new_window_title(self, browser):
        WebDriverWait(browser, 10).until(expected_conditions.title_is('Дзен'))

    @allure.step("Verify the URL starts with 'https://dzen.ru/?yredirect=true'")
    def verify_new_window_url(self, browser):
        assert browser.current_url.startswith("https://dzen.ru/?yredirect=true")


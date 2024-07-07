import allure
import pytest
from Sprint_6.config import WEB_LINK
from Sprint_6.pages.scooter_order_pages_from_the_end import OrderPage
from .order_helpers import confirm_order
from .test_data import test_order_data_2


@pytest.mark.parametrize("name, surname, address, subway, phone", test_order_data_2)
@allure.feature('Order Scooter')
@allure.story('Order Scooter from the End of Home Screen')
class TestOrderScooterFromTheEndOfHomeScreen:
    @allure.title('Test order scooter from the end of home screen')
    @allure.step('Test step: Order scooter from the end of home screen')
    def test_order_scooter_from_the_end_of_home_screen(self, browser, name, surname, address, subway, phone):
        order_page = OrderPage(browser)
        browser.get(WEB_LINK)
        allure.step('Accept cookies')
        order_page.accept_cookies()
        allure.step('Click on the lower order button')
        order_page.click_lower_order_button()
        allure.step('Fill in personal information')
        order_page.fill_personal_info(name, surname, address, subway, phone)
        allure.step('Fill in rent information')
        order_page.fill_rent_info()
        allure.step('Confirm the order')
        confirm_order(browser)

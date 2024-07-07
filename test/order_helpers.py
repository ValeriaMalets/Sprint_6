from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.locators.scooter_order_locators import (form_order_button, confirmation_modal_window, button_yes,
                                                      order_complete_modal_window)


def confirm_order(browser):
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, form_order_button))).click()
    WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, confirmation_modal_window)))
    WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, button_yes))).click()
    WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, order_complete_modal_window)))
    view_status_button_xpath = f"{order_complete_modal_window}//button[contains(text(), 'Посмотреть статус')]"
    view_status_button = browser.find_element(By.XPATH, view_status_button_xpath)
    assert view_status_button.is_displayed(), "Кнопка 'Посмотреть статус' не отображается"
    view_status_button.click()

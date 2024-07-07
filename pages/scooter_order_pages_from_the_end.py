import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Sprint_6.locators.scooter_order_locators import (cookie_consent_button, order_for_whom_header, input_name,
                                                      input_surname, input_address, input_subway_name,
                                                      subway_dropdown_option_template, input_phone_number, next_button,
                                                      order_about_rent_header, input_date, current_date, input_term,
                                                      dropdown_option_2, input_comment, checkbox_gray, order_step_4,
                                                      lower_order_button)


class OrderPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Accept cookies')
    def accept_cookies(self):
        cookie_button = WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, cookie_consent_button))
        )
        cookie_button.click()

    @allure.step('Click on the lower order button')
    def click_lower_order_button(self):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, order_step_4))
        )

        element = self.browser.find_element(By.XPATH, order_step_4)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, lower_order_button))
        ).click()

    @allure.step('Fill in personal information')
    def fill_personal_info(self, name, surname, address, subway, phone):
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, order_for_whom_header))
        )
        self.browser.find_element(By.XPATH, input_name).send_keys(name)
        self.browser.find_element(By.XPATH, input_surname).send_keys(surname)
        self.browser.find_element(By.XPATH, input_address).send_keys(address)
        subway_input = self.browser.find_element(By.XPATH, input_subway_name)
        subway_input.send_keys(subway)
        subway_option_xpath = subway_dropdown_option_template.format(subway=subway)
        subway_option = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, subway_option_xpath))
        )
        subway_option.click()
        self.browser.find_element(By.XPATH, input_phone_number).send_keys(phone)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, next_button))
        ).click()

    @allure.step('Fill in rent information')
    def fill_rent_info(self):
        WebDriverWait(self.browser, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, order_about_rent_header))
        )
        self.browser.find_element(By.XPATH, input_date).click()
        self.browser.find_element(By.XPATH, current_date).click()
        self.browser.find_element(By.XPATH, input_term).click()
        WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, dropdown_option_2))
        ).click()
        WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, checkbox_gray))
        ).click()
        self.browser.find_element(By.XPATH, input_comment).send_keys('Test Test')

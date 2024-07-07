import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from Sprint_6.locators.scooter_important_questions_section_locators import important_questions_section_header


@allure.step('Scroll to the important questions section and click on a question')
def scroll_and_click(browser, question_button_xpath, answer_xpath):
    allure.step('Find the important questions section header and scroll to it')
    important_section_header = browser.find_element(By.XPATH, important_questions_section_header)
    browser.execute_script("arguments[0].scrollIntoView(true);", important_section_header)
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of(important_section_header))

    allure.step('Click on the question button')
    question_button = WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, question_button_xpath)))
    question_button.click()

    allure.step('Verify the answer is displayed')
    answer_element = WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, answer_xpath)))
    assert answer_element.is_displayed()

import allure
from config import WEB_LINK
from Sprint_6.pages.scooter_important_question_page import scroll_and_click

from Sprint_6.locators.scooter_important_questions_section_locators import (
    answer_question_1, important_question_button_1, important_question_button_2,
    answer_question_2, important_question_button_3, answer_question_3,
    important_question_button_4, answer_question_4, important_question_button_5,
    answer_question_5, important_question_button_6, answer_question_6,
    important_question_button_7, answer_question_7, important_question_button_8, answer_question_8
)

@allure.feature('Important Questions Section')
@allure.story('User interacts with important questions')
class TestScooterImportantQuestionSection:

    @allure.title('Test important question 1')
    def test_important_question_1(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_1, answer_question_1)

    @allure.title('Test important question 2')
    def test_important_question_2(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_2, answer_question_2)

    @allure.title('Test important question 3')
    def test_important_question_3(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_3, answer_question_3)

    @allure.title('Test important question 4')
    def test_important_question_4(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_4, answer_question_4)

    @allure.title('Test important question 5')
    def test_important_question_5(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_5, answer_question_5)

    @allure.title('Test important question 6')
    def test_important_question_6(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_6, answer_question_6)

    @allure.title('Test important question 7')
    def test_important_question_7(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_7, answer_question_7)

    @allure.title('Test important question 8')
    def test_important_question_8(self, browser):
        browser.get(WEB_LINK)
        scroll_and_click(browser, important_question_button_8, answer_question_8)

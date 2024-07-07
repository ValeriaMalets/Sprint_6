# Scooter Home Page
upper_order_button = ('//div[contains(@class, "Header_Nav__AGCXC")]//button[contains(@class, "Button_Button__ra12g") '
                      'and text()="Заказать"]')
lower_order_button = ('//div[contains(@class, "Home_FinishButton__1_cWm")]//button[contains(@class, '
                      '"Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')
status_button = ('//div[contains(@class, "Header_Nav__AGCXC")]//button[contains(@class, "Header_Link__1TAG7") and '
                 'text()="Статус заказа"]')
order_step_4 = '//div[.//div[text()="Курьер забирает самокат"] and .//div[text()="Когда аренда заканчивается"]]'


# Scooter Order Form Part1 FOR WHOM
order_for_whom_header = '//div[contains(@class, "Order_Header__BZXOb") and text()="Для кого самокат"]'
input_name = '//input[@placeholder="* Имя"]'
input_surname = '//input[@placeholder="* Фамилия"]'
input_address = '//input[@placeholder="* Адрес: куда привезти заказ"]'
input_subway_name = '//input[@placeholder="* Станция метро"]'
input_phone_number = '//input[@placeholder="* Телефон: на него позвонит курьер"]'
input_subway_name = '//input[@placeholder="* Станция метро"]'
subway_dropdown_option_template = ("//div[contains(@class, 'select-search__select')]/ul/li/button/div[contains(text(), "
                                   "'{subway}')]")
next_button = '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Далее"]'
cookie_consent_button = '//button[@id="rcc-confirm-button"]'


# Scooter Order Form Part2 ABOUT RENT
order_about_rent_header = '//div[contains(@class, "Order_Header__BZXOb") and text()="Про аренду"]'
input_date = '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN"]'
current_date = '//div[contains(@class, "react-datepicker__day") and contains(@class, "react-datepicker__day--today")]'
input_term = '//div[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]'
dropdown_option_1 = ('//div[contains(@class, "Dropdown-menu")]//div[contains(@class, "Dropdown-option") and text('
                     ')="двое суток"]')
dropdown_option_2 = ('//div[contains(@class, "Dropdown-menu")]//div[contains(@class, "Dropdown-option") and text('
                     ')="трое суток"]')
input_color = '//div[@class="Order_Title__3EKne" and text()="Цвет самоката"]'
checkbox_black = '//label[contains(text(), "чёрный жемчуг")]/input[@type="checkbox"]'
checkbox_gray = '//label[contains(text(), "серая безысходность")]/input[@type="checkbox"]'
input_comment = '//input[@placeholder="Комментарий для курьера"]'
form_order_button = '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'


# Confirm order modal window
confirmation_modal_window = ('//div[@class="Order_Modal__YZ-d3" and .//div[@class="Order_ModalHeader__3FDaJ" and '
                             'contains(text(), "Хотите оформить заказ?")]]')
button_yes = '//button[contains(text(), "Да")]'

# Success Modal Window
order_complete_modal_window = ('//div[@class="Order_Modal__YZ-d3" and .//div[@class="Order_ModalHeader__3FDaJ" and '
                               'contains(text(), "Заказ оформлен")]]')

order_next_status_button = ('//button[contains(text(), "Посмотреть статус") and contains(@class, '
                            '"Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM")]')

# Logo for following to corresponding website screens
scooter_logo = '//a[contains(@class, "Header_LogoScooter__3lsAR") and .//img[contains(@src, "/assets/scooter.svg")]]'
yandex_logo = '//a[contains(@class, "Header_LogoYandex__3TSOI") and .//img[contains(@src, "/assets/ya.svg")]]'

dzen_find_button = ('//form[contains(@class, "arrow")]//button[contains(@class, "arrow__button") and @type="submit" '
                    'and text()="Найти"]')



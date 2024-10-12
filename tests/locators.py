from selenium.webdriver.common.by import By


def find_element_by_xpath(driver_start, xpath):
    element = driver_start.find_element(By.XPATH, xpath)
    return element

def find_elements_by_xpath(driver_start, xpath):
    elements = driver_start.find_elements(By.XPATH, xpath)
    return elements

def find_element_by_link_text(driver_start, link_text):
    element = driver_start.find_element(By.LINK_TEXT, link_text)
    return element

class Locators:
    fields_for_registration = ".//input[@class='text input__textfield text_type_main-default']"
    # # Поля для ввода в форме регистрации (имя, почта, пароль)

    reg_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    # # Кнопка "Зарегистрироваться"

    fields_for_login = ".//input[@class='text input__textfield text_type_main-default']"
    # Поля для ввода в форме логина (почта, пароль)

    login_button = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    # Кнопка "Войти" на странице логина

    personal_account = "Личный Кабинет"
    # Кнопка "Личный кабинет"

    profile = "Профиль"
    # Кнопка "Профиль" в личном кабинете

    error_message = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    # Текст "Некорректный пароль" на странице регистрации

    exit_button = ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    # Кнопка "Выход" в личном кабинете

    go_in_text = ".//h2[text()='Вход']"
    # Текст "Войти" на странице логина

    another_personal_account = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    # Текст "Войти" на странице логина

    go_in_button_in_registration_page = "Войти"
    # кнопка "Войти" на странице регистрации

    go_in_button_in_recovery_password_page = ".//a[@class='Auth_link__1fOlj']"
    # кнопка "Войти" на странице востановления пароля

    logo = ".//a"
    # Логотип

    constructor = ".//p[text()='Конструктор']"
    # Раздел "Конструктор"

    assemble_the_burger = ".//h1[text()='Соберите бургер']"
    # Текст 'Соберите бургер'

    active_section_in_constructor = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    # Активная секция в конструкторе

    inactive_sections_in_constructor = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']"
    # Неактивная секции в конструкторе

    text_in_constructor_section = ".//span"
    # Текст "Булки"/"Соусы"/"Начинки"




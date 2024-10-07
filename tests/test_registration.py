from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from randomizer import *


current_mail = gen_email()
current_pass = gen_pass()
print(current_mail)
print(current_pass)

def test_registration(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/register"
    driver_start.get(current_url)
    input_fields = driver_start.find_elements(By.XPATH,
    ".//input[@class='text input__textfield text_type_main-default']")
    input_fields[0].send_keys('Maxim')
    input_fields[1].send_keys(current_mail)
    input_fields[2].send_keys(current_pass)
    print(current_mail)
    print(current_pass)
    reg_button = driver_start.find_element(By.XPATH,
    ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    reg_button.click()
    driver_start.implicitly_wait(3)
    driver_start.get("https://stellarburgers.nomoreparties.site/login")
    input_fields = driver_start.find_elements(By.XPATH,
    ".//input[@class='text input__textfield text_type_main-default']")
    input_fields[0].send_keys(current_mail)
    input_fields[1].send_keys(current_pass)
    print(current_mail)
    print(current_pass)
    driver_start.find_element(By.XPATH,
    ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    driver_start.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver_start.find_element(By.LINK_TEXT, "Профиль").click()
    assert "/account/profile" in driver_start.current_url


def test_incorrect_password(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/register"
    driver_start.get(current_url)
    input_fields = driver_start.find_elements(By.XPATH,
    ".//input[@class='text input__textfield text_type_main-default']")
    input_fields[0].send_keys('Maxim')
    input_fields[1].send_keys(current_mail)
    input_fields[2].send_keys('123')
    reg_button = driver_start.find_element(By.XPATH,
    ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    reg_button.click()
    driver_start.implicitly_wait(3)
    error_message = WebDriverWait(driver_start, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH,
    ".//p[@class='input__error text_type_main-default']"))).text
    assert error_message == "Некорректный пароль"

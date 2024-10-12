from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from test_data import *
from links import *


def test_registration(driver_start, current_mail, current_pass):
    driver_start.get(registration_url)
    input_fields_for_registration = find_elements_by_xpath(driver_start, Locators.fields_for_registration)
    input_fields_for_registration[0].send_keys(valid_name)
    input_fields_for_registration[1].send_keys(current_mail)
    input_fields_for_registration[2].send_keys(current_pass)
    find_element_by_xpath(driver_start, Locators.reg_button).click()
    driver_start.implicitly_wait(3)
    driver_start.get(login_url)
    input_fields_for_login = driver_start.find_elements(By.XPATH, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(current_mail)
    input_fields_for_login[1].send_keys(current_pass)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_link_text(driver_start, Locators.profile).click()
    assert "/account/profile" in driver_start.current_url

def test_incorrect_password(driver_start, current_mail):
    driver_start.get(registration_url)
    input_fields_for_registration = find_elements_by_xpath(driver_start, Locators.fields_for_registration)
    input_fields_for_registration[0].send_keys(valid_name)
    input_fields_for_registration[1].send_keys(current_mail)
    input_fields_for_registration[2].send_keys(not_correct_password)
    find_element_by_xpath(driver_start, Locators.reg_button).click()
    driver_start.implicitly_wait(3)
    error_message = WebDriverWait(driver_start, 3).until(expected_conditions.visibility_of_element_located((Locators.error_message))).text
    assert error_message == "Некорректный пароль"

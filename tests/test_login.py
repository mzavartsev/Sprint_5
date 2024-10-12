from locators import *
from test_data import *
from links import *


def test_login_personal_account_button(driver_start):
    driver_start.get(main_url)
    find_element_by_xpath(driver_start, Locators.another_personal_account).click()
    driver_start.implicitly_wait(3)
    input_fields_for_login = find_elements_by_xpath(driver_start, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(valid_mail)
    input_fields_for_login[1].send_keys(valid_password)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_link_text(driver_start, Locators.profile).click()
    assert "/account/profile" in driver_start.current_url

def test_login_registration_form(driver_start):
    driver_start.get(registration_url)
    find_element_by_link_text(driver_start, Locators.go_in_button_in_registration_page).click()
    driver_start.implicitly_wait(3)
    input_fields_for_login = find_elements_by_xpath(driver_start, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(valid_mail)
    input_fields_for_login[1].send_keys(valid_password)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_link_text(driver_start, Locators.profile).click()
    assert "/account/profile" in driver_start.current_url

def test_login_to_account_button(driver_start):
    driver_start.get(main_url)
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    driver_start.implicitly_wait(3)
    input_fields_for_login = driver_start.find_elements(By.XPATH, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(valid_mail)
    input_fields_for_login[1].send_keys(valid_password)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_link_text(driver_start, Locators.profile).click()
    assert "/account/profile" in driver_start.current_url

def test_login_forgot_password(driver_start):
    driver_start.get(forgot_password_url)
    find_element_by_xpath(driver_start, Locators.go_in_button_in_recovery_password_page).click()
    driver_start.implicitly_wait(3)
    input_fields_for_login = driver_start.find_elements(By.XPATH, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(valid_mail)
    input_fields_for_login[1].send_keys(valid_password)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_xpath(driver_start, Locators.exit_button).click()
    assert "/account/profile" in driver_start.current_url

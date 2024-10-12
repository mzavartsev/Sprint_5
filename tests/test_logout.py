from locators import *
from test_data import *
from links import *


def test_logout(driver_start):
    driver_start.get(main_url)
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    driver_start.implicitly_wait(3)
    input_fields_for_login = driver_start.find_elements(By.XPATH, Locators.fields_for_login)
    input_fields_for_login[0].send_keys(valid_mail)
    input_fields_for_login[1].send_keys(valid_password)
    find_element_by_xpath(driver_start, Locators.login_button).click()
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    find_element_by_xpath(driver_start, Locators.exit_button).click()
    inscription = find_element_by_xpath(driver_start, Locators.go_in_text)
    assert inscription.is_displayed()


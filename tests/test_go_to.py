from locators import *
from links import *


def test_go_to_logo(driver_start):
    driver_start.get(login_url)
    find_element_by_xpath(driver_start, Locators.logo).click()
    assert driver_start.current_url == "https://stellarburgers.nomoreparties.site/"

def test_go_to_constructor(driver_start):
    driver_start.get(login_url)
    find_element_by_xpath(driver_start, Locators.constructor).click()
    assemble_the_burger = find_element_by_xpath(driver_start, Locators.assemble_the_burger)
    assert assemble_the_burger.is_displayed()

def test_go_to_personal_account(driver_start):
    driver_start.get(main_url)
    find_element_by_link_text(driver_start, Locators.personal_account).click()
    driver_start.implicitly_wait(3)
    assert driver_start.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_go_to_buns(driver_start):
    driver_start.get(main_url)
    driver_start.implicitly_wait(3)
    active_section = find_element_by_xpath(driver_start, Locators.active_section_in_constructor)
    buns = active_section.find_element(By.XPATH, Locators.text_in_constructor_section).text
    assert "Булки" == buns

def test_go_to_filling(driver_start):
    driver_start.get(main_url)
    inactive_sections = find_elements_by_xpath(driver_start, Locators.inactive_sections_in_constructor)
    inactive_sections[1].click()
    active_section = find_element_by_xpath(driver_start, Locators.active_section_in_constructor)
    filling = active_section.find_element(By.XPATH, Locators.text_in_constructor_section).text
    assert "Начинки" == filling

def test_go_to_sauce(driver_start):
    driver_start.get(main_url)
    inactive_sections = find_elements_by_xpath(driver_start, Locators.inactive_sections_in_constructor)
    inactive_sections[0].click()
    active_section = find_element_by_xpath(driver_start, Locators.active_section_in_constructor)
    sauses = active_section.find_element(By.XPATH, Locators.text_in_constructor_section).text
    assert "Соусы" == sauses

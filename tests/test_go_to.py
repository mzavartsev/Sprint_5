from selenium.webdriver.common.by import By


def test_go_to_constructor_and_logo(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/login"
    driver_start.get(current_url)
    driver_start.find_element(By.XPATH, ".//a").click()
    assert driver_start.current_url == "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    driver_start.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    assert driver_start.current_url == "https://stellarburgers.nomoreparties.site/"

def test_go_to_personal_account(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    driver_start.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver_start.implicitly_wait(3)
    assert driver_start.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_go_to_buns(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    inactive_sections = driver_start.find_elements(By.XPATH,
    ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    inactive_sections[1].click()
    filling = driver_start.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10']")
    inactive_sections = driver_start.find_elements(By.XPATH,
    ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    inactive_sections[0].click()
    buns = driver_start.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10']")
    assert True == buns.is_displayed()

def test_go_to_filling(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    inactive_sections = driver_start.find_elements(By.XPATH,
    ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    inactive_sections[1].click()
    filling = driver_start.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10']")
    assert True == filling.is_displayed()

def test_go_to_sauce(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    inactive_sections = driver_start.find_elements(By.XPATH,
    ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    inactive_sections[1].click()
    filling = driver_start.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10']")
    inactive_sections = driver_start.find_elements(By.XPATH,
    ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    inactive_sections[1].click()
    sauses = driver_start.find_element(By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10']")
    assert True == sauses.is_displayed()

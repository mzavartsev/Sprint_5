from selenium.webdriver.common.by import By


def test_logout(driver_start):
    current_url = "https://stellarburgers.nomoreparties.site/"
    driver_start.get(current_url)
    driver_start.find_element(By.LINK_TEXT,"Личный Кабинет").click()
    driver_start.implicitly_wait(3)
    input_fields = driver_start.find_elements(By.XPATH,
    ".//input[@class='text input__textfield text_type_main-default']")
    input_fields[0].send_keys('maksimzavartsev14556@yandex.ru')
    input_fields[1].send_keys('qweqwe123')
    driver_start.find_element(By.XPATH,
    ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    driver_start.find_element(By.LINK_TEXT,"Личный Кабинет").click()
    driver_start.find_element(By.XPATH,
    ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
    inscription = driver_start.find_element(By.XPATH, ".//h2[text()='Вход']")
    assert inscription.is_displayed()

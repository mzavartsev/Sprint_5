import pytest
from selenium import webdriver


@pytest.fixture
def driver_start():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from randomizer import *

@pytest.fixture
def driver_start():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def current_mail():
    return gen_email()
@pytest.fixture
def current_pass():
    return gen_pass()
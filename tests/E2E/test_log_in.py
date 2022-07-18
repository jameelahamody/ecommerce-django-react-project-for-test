import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    firefox_driver_binary = "geckodriver.exe"
    driver = webdriver.Firefox(executable_path=firefox_driver_binary)
    yield driver
    driver.close()
@pytest.mark.parametrize('account', ["HAMODYJAMEELA@GMAIL.COM"])
def test_user_login(driver, account):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    driver.find_element(By.ID, "email").click()
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("hamodyjameela@gmail.com")
    time.sleep(2)
    driver.find_element(By.ID, "password").click()
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("jameela58@")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(2)
    username = driver.find_element(By.CSS_SELECTOR, "#username").text
    user_of_login = username
    assert account in user_of_login
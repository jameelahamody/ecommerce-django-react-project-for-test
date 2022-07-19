import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
@pytest.fixture()
def driver():
    firefox_driver_binary = "geckodriver.exe"
    driver = webdriver.Firefox(executable_path=firefox_driver_binary)
    yield driver
    driver.close()

@pytest.mark.parametrize('account', ["OMAR"])
def test_user_create_account(driver,account):
    rnum = random.randint(5,100)
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    time.sleep(3)
    driver.execute_script("document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
    button = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
    time.sleep(3)
    button.click()
    time.sleep(3)
    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("omar")
    time.sleep(3)
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("test_of_"+str(rnum)+"register@gmail.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("hamody567@")
    driver.find_element(By.ID, "passwordConfirm").click()
    driver.find_element(By.ID, "passwordConfirm").send_keys("hamody567@")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(5)
    username = driver.find_element(By.CSS_SELECTOR, "#username").text
    user_of_login = username
    assert account in user_of_login

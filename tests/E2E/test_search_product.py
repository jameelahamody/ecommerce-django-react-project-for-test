
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.fixture()
# def driver():
#     firefox_driver_binary = "geckodriver.exe"
#     driver = webdriver.Firefox(executable_path=firefox_driver_binary)
#     yield driver
#     driver.close()
  
def test_search_product(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.set_window_size(1549, 925)
    expected_proc = driver.find_element(By.NAME, "q").text
    time.sleep(2)
    driver.find_element(By.NAME, "q").click()
    driver.find_element(By.NAME, "q").send_keys("red roses")
    driver.find_element(By.CSS_SELECTOR, ".p-2").click()
    time.sleep(2)
    search_proc = driver.find_element(By.NAME, "q").text
    assert search_proc == expected_proc
def test_fail():
  assert 2 == 1
    
  

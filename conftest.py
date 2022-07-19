import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture()
def driver():
    firefox_driver_binary = "geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()
    firefox_options.add_argument("--headless")
    browser_name = 'firefox'
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":

        dc = {
            "browserName": "firefox",
            "platformName": ""
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)
    yield driver
    driver.close()

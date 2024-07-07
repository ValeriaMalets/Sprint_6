import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
import sys
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def firefox_driver_path():
    path = GeckoDriverManager().install()
    return path


@pytest.fixture(scope="function")
def browser(firefox_driver_path):
    service = FirefoxService(executable_path=firefox_driver_path)
    options = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(service=service, options=options)

    yield driver

    driver.quit()

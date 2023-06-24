import os.path
import time
import zipfile
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from conftest import TMP_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_file_with_browser():
    options = webdriver.ChromeOptions()
    prefs = {
    "download.default_directory": TMP_PATH,
    "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(1)

    size_file = os.path.getsize(os.path.join(TMP_PATH, 'pytest-main.zip'))
    assert size_file == 1567875

    with zipfile.ZipFile(os.path.join(TMP_PATH, 'pytest-main.zip'), 'r') as zip_file:
        expected_files = ['pytest-main/']
    assert all(file in zip_file.namelist() for file in expected_files)

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def accept_cookies(driver):
    try:
        wait = WebDriverWait(driver, 10)
        cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "sp-cc-accept")))
        cookie_btn.click()
    except Exception:
        pass

def test_open_page(driver): # Zmiana nazwy na unikalną
    driver.get('https://www.amazon.pl/')
    accept_cookies(driver)
    assert "Amazon.pl" in driver.title

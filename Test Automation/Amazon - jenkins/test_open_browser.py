import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
    """Pomocnicza funkcja do akceptacji cookies."""
    try:
        wait = WebDriverWait(driver, 10)
        cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "sp-cc-accept")))
        cookie_btn.click()
        print("Cookies accepted.")
    except Exception as e:
        print(f"Banner not found or error: {e}")

def test_run_test(driver):
    url = 'https://www.amazon.pl/'
    driver.get(url)
    
    try:
        accept_cookies(driver)
        title = driver.title
        print(f"Page title: {title}")
        assert "Amazon.pl" in title
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

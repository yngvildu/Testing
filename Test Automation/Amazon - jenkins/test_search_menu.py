from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_open_browser import accept_cookies

def test_search_menu(driver):
    url = 'https://www.amazon.pl/'
    driver.get(url)
    accept_cookies(driver)
    wait = WebDriverWait(driver, 10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID, "nav-hamburger-menu")))
    menu_btn.click()
    category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Książki']")))
    category_btn.click()
    polishbooks_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.hmenu-item[href*='polish']")))       
    driver.execute_script("arguments[0].click();", polishbooks_btn)
    assert "polish" in driver.current_url.lower()
    print("Test passed: Polish books section reached.")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains
from Open_Browser import *

def add_product():
    driver = get_driver()
    url = 'https://www2.hm.com/pl_pl/index.html'

    try:
        driver.get(url)
        accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        header_btn = wait.until(EC.element_to_be_clickable((By.ID, "header-search-button")))
        header_btn.click()
        site_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#site-search")))
        site_form.send_keys("biała bluzka damska")
        site_form.send_keys(Keys.ENTER)
        wait.until(EC.url_contains("search-results"))
        print(f"Current URL: {driver.current_url}")
        assert "search-results" in driver.current_url
        product_selector = "article.product-item a"
        blouse_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, product_selector)))
        blouse_btn.click()
        wait.until(EC.url_contains("productpage"))
        assert "productpage" in driver.current_url
        size_btn = wait.until(EC.element_to_be_clickable((By.ID, "sizeButton-2")))
        size_btn.click()
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-bag-button")))
        add_btn.click()
        print("Succesfully added to chart")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    add_product()     
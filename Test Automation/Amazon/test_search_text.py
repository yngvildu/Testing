from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from test_open_browser import *

def test_search():
    driver = test_get_driver()
    url = 'https://www.amazon.pl/'

    try:
        driver.get(url)
        test_accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        site_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#twotabsearchtextbox")))  
        site_form.send_keys("suszarka dyson")
        site_form.send_keys(Keys.ENTER) 
        wait = WebDriverWait(driver, 10)
        assert "suszarka" in driver.current_url
        print("Search submitted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_search() 

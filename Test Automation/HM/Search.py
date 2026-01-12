from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from Open_Browser import * 

def search():
    driver = get_driver()
    url = 'https://www2.hm.com/pl_pl/index.html'

    try:
        driver.get(url)
        accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        header_btn = wait.until(EC.element_to_be_clickable((By.ID, "header-search-button")))
        header_btn.click()
        site_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#site-search")))  
        site_form.send_keys("spodnie dresowe")
        site_form.send_keys(Keys.ENTER) 
        print("Search submitted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    search() 
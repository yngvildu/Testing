from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def accept_cookies(driver):
    try:
        wait = WebDriverWait(driver, 10)
        cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "banner-accept-btn")))
        cookie_btn.click()
        print("Cookies accepted successfully.")
    except Exception as e:
        print(f"Cookies banner did not appear or error occurred: {e}")

def run_test():
    driver = get_driver()
    url = 'https://www2.hm.com/pl_pl/index.html'
    
    try:
        driver.get(url)
        accept_cookies(driver)
        title = driver.title
        print(f"Page title: {title}")
        assert "H&M" in title
        
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    run_test()
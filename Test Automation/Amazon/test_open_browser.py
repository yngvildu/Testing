from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def test_get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def test_accept_cookies(driver):
    try:
        wait = WebDriverWait(driver, 10)
        cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "sp-cc-accept")))
        cookie_btn.click()
        print("Cookies accepted successfully.")
    except Exception as e:
        print(f"Cookies banner did not appear or error occurred: {e}")

def test_run_test():
    driver = test_get_driver()
    url = 'https://www.amazon.pl/'
    
    try:
        driver.get(url)
        accept_cookies(driver)
        title = driver.title
        print(f"Page title: {title}")
        assert "Amazon.pl" in title
        
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_run_test()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from Open_browser import * 

def search_board_game():
    driver = get_driver()
    url = 'https://www.amazon.pl/'

    try:
        driver.get(url)
        accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        site_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#twotabsearchtextbox")))  
        site_form.send_keys("gra planszowa")
        site_form.send_keys(Keys.ENTER) 
        assert "gra" in driver.current_url
        checkbox_icon = driver.find_element(By.CSS_SELECTOR, "div.a-checkbox i.a-icon-checkbox")
        checkbox_icon.click()
        print("Checkbox is marked")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    search_board_game() 
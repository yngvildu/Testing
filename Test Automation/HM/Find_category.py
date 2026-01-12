from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Open_Browser import *

def find_category():
    driver = get_driver()
    url = 'https://www2.hm.com/pl_pl/index.html'

    try:
        driver.get(url)
        accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        ladies = wait.until(EC.visibility_of_element_located((By.ID, "ladies"))) 
        actions.move_to_element(ladies).perform()
        ladies_accesories_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, r"#ladies-accessories-\/pl_pl\/ona\/dodatki\.html")))
        ladies_accesories_btn.click()
        juwelery_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, r"#ladies-accessories-jewellery-\/pl_pl\/ona\/dodatki\/bizuteria\.html")))
        juwelery_btn.click()
        print("Successfully navigated to jewelry.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")
    
if __name__ == "__main__":
    find_category() 
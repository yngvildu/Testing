from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_open_browser import accept_cookies
import time

def test_add_product(driver):
    wait = WebDriverWait(driver, 20)

    try:
        driver.get('https://www.amazon.pl/')
        test_accept_cookies(driver)
        wait = WebDriverWait(driver, 10)
        search_bar = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
        search_bar.send_keys("Biblia")
        search_bar.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        product_link_xpath = "(//div[@data-component-type='s-search-result']//h2/a)[1]"
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, product_link_xpath)))
        product_url = first_product.get_attribute("href")
        driver.get(product_url)
        wait = WebDriverWait(driver, 10)
        add_btn_xpath = "//input[@id='add-to-cart-button'] | //button[@id='add-to-cart-button'] | //input[@name='submit.add-to-cart'] | //input[@id='buybox-see-all-buying-choices-announce']"
        add_btn = wait.until(EC.presence_of_element_located((By.XPATH, add_to_cart_xpath)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_btn)
        wait = WebDriverWait(driver, 10)
        driver.execute_script("arguments[0].click();", add_btn)
        side_cart_xpath = "//input[@name='submit.addToCart']"
        side_btn = wait.until(EC.element_to_be_clickable((By.XPATH, side_cart_xpath)))
        driver.execute_script("arguments[0].click();", side_btn)    
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.amazon.pl/gp/cart/view.html")
        wait.until(EC.url_contains("cart"))
        print("Success")

    except Exception as e:
        print(f"Error: {e}")

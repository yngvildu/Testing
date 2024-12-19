import selenium
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
driver.get('https://skleptest.pl')
driver.maximize_window()
title = driver.title
print(title)
assert 'Generic Shop' in driver.title
driver.quit()


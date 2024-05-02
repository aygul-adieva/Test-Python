from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p")
button.click()

sleep(5)
driver.quit()
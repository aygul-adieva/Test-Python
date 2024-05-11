from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid/")

for n in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()


from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http//:uitestingplayground.com/dynamicid/")

for n in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()


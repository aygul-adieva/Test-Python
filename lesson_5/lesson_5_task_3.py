from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(), Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

for n in range(5):
    button.click()
    sleep(1)
sleep(5)


delete_button = driver.find_elements(By.XPATH, '//button[contains)text(), "Delete"]')

print(f"Размер списка, {len(delete_button)}")
driver.quit()



from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(""http://the-internet.herokuapp.com/add_remove_elements/"")
Add_Element = "//button[contains(text(), Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

for n in range(5):
    button.click()
    sleep(1)
sleep(5)

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(), "Delete")]')

print(f"Размер списка, {len(delete_button)}")
driver.quit()


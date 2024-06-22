from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, value="#newButtonName").send_keys("ScyPro")
driver.find_element(By.CSS_SELECTOR, value='#updatingButton').click()
button = driver.find_element(By.CSS_SELECTOR, value='#updatingButton').text

print(button)

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By



@pytest.fixture

def driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()



def test_form_submission(driver):

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')



    driver.find_element(By.NAME, 'firstname').send_keys('Иван')

    driver.find_element(By.NAME, 'lastname').send_keys('Петров')

    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')

    driver.find_element(By.NAME, 'email').send_keys('test@scypro.com')

    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')

    driver.find_element(By.NAME, 'city').send_keys('Москва')

    driver.find_element(By.NAME, 'country').send_keys('Россия')

    driver.find_element(By.NAME, 'job').send_keys('QA')

    driver.find_element(By.NAME, 'company').send_keys('SkyPro')



    submit_button = driver.find_element(By.NAME, 'submit')

    submit_button.click()



    # Проверка подсвечивания полей

    zip_code_field = driver.find_element(By.NAME, 'zip')

    assert 'has-error' in zip_code_field.get_attribute('class')



    error_class = 'has-success'

    fields_to_check = ['firstname', 'lastname', 'address', 'email', 'phone', 'city', 'country', 'job', 'company']



    for field_name in fields_to_check:

        field = driver.find_element(By.NAME, field_name)

        assert error_class in field.get_attribute('class')
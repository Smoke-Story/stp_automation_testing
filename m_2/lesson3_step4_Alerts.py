import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def calculate(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

with webdriver.Chrome() as driver:
    driver.get('https://suninjuly.github.io/alert_accept.html')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    driver.switch_to.alert.accept()
    sleep(0.5)  # чуть ожидания загрузки новой страницы
    x_value = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(calculate(x_value))
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click()
    print(''.join(driver.switch_to.alert.text))
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    x_value = driver.find_element(By.ID, 'treasure').get_attribute('valuex')
    req = driver.find_element(By.ID, 'answer').get_attribute('required')
    dis = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').get_attribute('disabled')
    print(x_value, req, dis)
    driver.find_element(By.ID, 'answer').send_keys(calculate(x_value))
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click()
    print(''.join(driver.switch_to.alert.text)) # результат будет в консоли

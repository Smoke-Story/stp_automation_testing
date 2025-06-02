import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calculate(value):
    return math.log(abs(12 * math.sin(int(value))))

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    x_value = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(str(calculate(x_value)))
    driver.find_element(By.ID, 'solve').click()
    print(''.join(driver.switch_to.alert.text))

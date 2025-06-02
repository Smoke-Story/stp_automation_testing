import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))

with webdriver.Chrome() as driver:
    driver.get('https://suninjuly.github.io/math.html')
    x = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    driver.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click() # path для разнообразия :D
    print(''.join(driver.switch_to.alert.text)) # выводим результат сразу в консоль, что бы не ждать.

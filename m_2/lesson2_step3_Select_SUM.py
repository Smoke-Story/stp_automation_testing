from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://suninjuly.github.io/selects1.html')
    # в val помещаем результат сложения 2-х чисел.
    val = int(driver.find_element(By.ID, 'num1').text) + int(driver.find_element(By.ID, 'num2').text)
    driver.find_element(By.ID, 'dropdown').click() # клик по списку
    driver.find_element(By.XPATH, f'//option[text()="{val}"]').click() # клик по элементу val
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click() # жмём на кнопку
    print(''.join(driver.switch_to.alert.text)) # вывод результата в консоль

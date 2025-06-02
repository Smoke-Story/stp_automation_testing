import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc_value(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

with webdriver.Chrome() as driver:
    driver.get('https://SunInJuly.github.io/execute_script.html')
    top_frame = driver.find_element(By.ID, 'input_value') # помещаем в переменную top_frame элемент с чилом x
    driver.execute_script('return arguments[0].scrollIntoView(true);', top_frame) # двигаем страницу
    driver.find_element(By.ID, 'answer').send_keys(calc_value(top_frame.text)) # отправляем текст из top_frame
    driver.find_element(By.ID, 'robotCheckbox').click() # клик по чекбоксу
    driver.find_element(By.ID, 'robotsRule').click()    # клик по радиобатончику
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click() # клик по кнопке
    print(''.join(driver.switch_to.alert.text)) # вывод результата в консоль

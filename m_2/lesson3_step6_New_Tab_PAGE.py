import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calculating(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

with webdriver.Chrome() as driver:
    driver.get('https://suninjuly.github.io/redirect_accept.html')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click() # клик по кнопке
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])                # переключаемся на новую вкладку
    sleep(1)                                                       # чуть ожидания загрузки новой страницы
    x_value = driver.find_element(By.ID, 'input_value').text   # получаем значение х для функции
    driver.find_element(By.ID, 'answer').send_keys(calculating(x_value))   # отправляем х в input
    sleep(1)
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click()    # клик по кнопке
    sleep(1)
    print(''.join(driver.switch_to.alert.text))                      # вывод результата в консоль

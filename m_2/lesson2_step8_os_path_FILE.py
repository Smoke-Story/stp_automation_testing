import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Ivan')
    driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Jackson')
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('jjjjjjj@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ggwp.txt')
    driver.find_element(By.XPATH, '//input[@id="file"]').send_keys(file_path)
    driver.find_element(By.XPATH, '//button[text()="Submit"]').click()
    print(''.join(driver.switch_to.alert.text))

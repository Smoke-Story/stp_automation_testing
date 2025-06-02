from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/find_xpath_form')
    fname = driver.find_element(By.XPATH, '//input[@name="first_name"]')
    fname.send_keys('Jonathan')
    lname = driver.find_element(By.XPATH, '//input[@name="last_name"]')
    lname.send_keys('Kuznetsov')
    city = driver.find_element(By.XPATH, '//input[@class="form-control city"]')
    city.send_keys('Minsk')
    country = driver.find_element(By.XPATH, '//input[@id="country"]')
    country.send_keys('Belarus')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    sleep(3)

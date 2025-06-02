from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:    # запуск драйвера в переменную и само-закрытие его после assert
    driver.get('http://suninjuly.github.io/registration2.html')
    fn = driver.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
    fn.send_keys('Jonathan')
    ln = driver.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
    ln.send_keys('Kuznetsov')
    em = driver.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
    em.send_keys('wegwvwevewv@fwfc.ru')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    sleep(1)
    welcome_text = driver.find_element(By.CSS_SELECTOR, 'h1').text
    assert 'Congratulations! You have successfully registered!' == welcome_text

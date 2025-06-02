from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/huge_form.html')
    labels = driver.find_elements(By.XPATH, '//div[@class="first_block"]/input')
    for _ in labels:
        _.send_keys('Это последнее?')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(0.2)

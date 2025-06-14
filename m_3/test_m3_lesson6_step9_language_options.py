from time import sleep
from selenium.webdriver.common.by import By
""" Настройки теста находятся в файле conftest.py """

def test_add_to_basket_button_exist(driver):
    driver.implicitly_wait(3)
    driver.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    check_button = driver.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert check_button is not None # проверка на присутствие кнопки
    sleep(5) # 5 сек, что бы успеть глянуть на языковую версию :)

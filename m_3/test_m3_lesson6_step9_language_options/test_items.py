from time import sleep
from selenium.webdriver.common.by import By

def test_add_to_basket_button_exist(browser):
    browser.implicitly_wait(3)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    check_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert check_button is not None # проверка на присутствие кнопки
    sleep(5) # 5 сек, что бы успеть глянуть на языковую версию :)

import pytest
from time import sleep
from selenium.webdriver.common.by import By

def test_item_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    sleep(3) # что бы можно было убедиться в версии "es"

import pytest
from selenium.webdriver.common.by import By


def test_item_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

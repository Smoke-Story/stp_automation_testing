"""pytest test_m3_lesson4_step5_fixture_scope.py - запустить этот файл в CMD"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

""" scope:   Для фикстур можно задавать область покрытия фикстур. 
Допустимые значения: “function”, “class”, “module”, “session”. 
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, 
один раз для модуля или один раз для всех тестов, запущенных в данной сессии. """

@pytest.fixture(scope="class")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit driver..")
    driver.quit()

class TestMainPage1:

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, driver):
        print("start test1")
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        print("start test2")
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

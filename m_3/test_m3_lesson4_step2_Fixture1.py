"""pytest -s test_m3_lesson4_step2_Fixture1.py - запустить этот файл в CMD"""

from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'

class TestMainPage1:

    @classmethod
    def setup_class(cls):
        print("\nstart browser for test suite 1..")
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite 1..")
        cls.driver.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.driver.get(link)
        self.driver.find_element(By.ID, 'login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

class TestMainPage2:

    def setup_method(self):
        print("\nstart browser for test 2..")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test 2..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.driver.get(link)
        self.driver.find_element(By.ID, 'login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.driver.get(link)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

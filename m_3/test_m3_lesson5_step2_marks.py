import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit driver..")
    driver.quit()

class TestMainPage1:

    # @pytest.mark.xfail(strict=True)
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link1(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link2(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.skip # тест помечен меткой "пропустить"
    def test_guest_should_see_login_link3(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link4(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page1(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now") # метка xfail
    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page2(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_search_button_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

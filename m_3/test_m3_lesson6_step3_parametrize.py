import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.parametrize("language", [
    "ru", "en-gb", "fr", "ge", "de"
])
def test_guest_should_see_login_link(driver, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, ".h1 a")

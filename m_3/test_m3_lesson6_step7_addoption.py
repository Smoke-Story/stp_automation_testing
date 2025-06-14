import pytest
from selenium.webdriver.common.by import By
""" Настройки теста находятся в файле conftest.py """

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")

if __name__ == "__main__":
    pytest.main()

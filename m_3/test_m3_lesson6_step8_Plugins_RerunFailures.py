from selenium.webdriver.common.by import By
""" Настройки теста находятся в файле conftest.py """

""" В этом тесте реализована работа плагина: 'pytest-rerunfailures'. 
Этот плагин позволяет при падении теста задавать *число(n) повторных проверок параметром: --reruns n """

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(driver):
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#magic_link")
from time import sleep
from selenium.webdriver.common.by import By

def test_add_to_basket_button_any_language(browser):

    languages = {
        'ar': 'أضف الى سلة التسوق',
        'ca': 'Afegeix a la cistella',
        "cs": 'Vložit do košíku',
        "da": 'Læg i kurv',
        'de': 'In Warenkorb legen',
        "en-gb": 'Add to basket',
        "el": 'Προσθήκη στο καλάθι',
        "es": 'Añadir al carrito',
        "fi": 'Lisää koriin',
        "fr": 'Ajouter au panier',
        "it": 'Aggiungi al carrello',
        "ko": '장바구니 담기',
        "nl": 'Voeg aan winkelmand toe',
        "pl": 'Dodaj do koszyka',
        "pt": 'Adicionar ao carrinho',
        "pt-br": 'Adicionar à cesta',
        "ro": 'Adauga in cos',
        "ru": 'Добавить в корзину',
        "sk": 'Pridať do košíka',
        "uk": 'Додати в кошик',
        "zh-hans": 'Add to basket'
    }
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    country = browser.find_element(By.TAG_NAME, "html").get_attribute("lang")   #проверка страны страницы
    check_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").text  # текст кнопки

    assert languages[country] == check_button   # проверка текста кнопки с текстом из словаря
    sleep(5) # 5 сек, что бы успеть глянуть на языковую версию :)

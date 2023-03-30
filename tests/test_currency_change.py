import pytest
from PageObject.elements.HeaderElement import HeaderElement
from PageObject.ProductCardPage import ProductCardPage
from utils import *
import allure


@allure.story("Тестовые сценарии")
@allure.title("Смена валюты на странице 'карточка продукта'")
@pytest.mark.slow
@pytest.mark.parametrize("product, prices", [("/iphone", IPHONE_PRICE), ("/macbook", MAC_PRICE)])
def test_currency_change(browser, product, prices):
    """
    1) зайти на продуктовую страницу
    2) сменить валюту на USD
    3) проверить что цена в USD корректна
    4) сменить валюту на EUR
    5) проверить что цена в EUR корректна
    6) сменить валюту на GBP
    7) проверить что цена в GBP корректна
    """

    price_dict = prices
    PRODUCT_CARD_PAGE = ProductCardPage(browser)

    with allure.step('1) зайти на продуктовую страницу'):
        PRODUCT_CARD_PAGE.open_(browser.url + product)

    with allure.step('2) сменить валюту на USD'):
        HeaderElement(browser).change_currency_to("USD")

    with allure.step('3) проверить что цена в USD корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["USD"]

    with allure.step('4) сменить валюту на EUR'):
        HeaderElement(browser).change_currency_to("EUR")

    with allure.step(' 5) проверить что цена в EUR корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["EUR"]

    with allure.step('6) сменить валюту на GBP'):
        HeaderElement(browser).change_currency_to("GBP")

    with allure.step('7) проверить что цена в GBP корректна'):
        assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["GBP"]

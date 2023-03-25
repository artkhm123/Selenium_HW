import time

import pytest
from PageObject.elements.HeaderElement import HeaderElement
from utils import *
from PageObject.ProductCardPage import ProductCardPage


@pytest.mark.parametrize("product, prices", [("/iphone", IPHONE_PRICE), ("/macbook", MAC_PRICE)])
def test_currency_change(browser, product, prices):
    """
    1) зайти на продуктовую страницу
    2) сменить валюту на USD корректна
    3) проверить что цена в USD корректна
    4) сменить валюту на EUR корректна
    5) проверить что цена в EUR корректна
    6) сменить валюту на GBP корректна
    7) проверить что цена в GBP корректна
    """

    PRODUCT_CARD_PAGE = ProductCardPage(browser)
    PRODUCT_CARD_PAGE.open(browser.url + product)

    price_dict = prices
    HeaderElement(browser).change_currency_to("USD")
    assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["USD"]
    HeaderElement(browser).change_currency_to("EUR")
    assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["EUR"]
    HeaderElement(browser).change_currency_to("GBP")
    assert PRODUCT_CARD_PAGE.get_product_price() == price_dict["GBP"]

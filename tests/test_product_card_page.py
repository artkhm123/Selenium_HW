import pytest
import allure
from PageObject.ProductCardPage import ProductCardPage


@allure.story("Тесты на поиск элементов")
@allure.title("Product Card. Проверка наличия элементов на странице.")
@pytest.mark.slow
@pytest.mark.parametrize("product", ["/iphone", "/macbook"])
def test_product_card_page(browser, product):
    # def test_product_card_page(browser):
    """
    Предусловие: в корзине нет товаров
    Тест: Поиск элементов
    1) Найдем значение которое отображается "в корзине" перед началом теста
    2) Найдем цену товара
    3) Найдем количество товара
    4) Найдем и кликнем по кнопке Add to cart
    5) Найдем новое значение "в корзине"
    """

    PRODUCT_CARD_PAGE = ProductCardPage(browser)
    PRODUCT_CARD_PAGE.open_(browser.url + product)

    with allure.step('1) Найдем значение которое отображается "в корзине" перед началом теста'):
        cart_counter_before = PRODUCT_CARD_PAGE.cart_counter()

    with allure.step('2) Найдем цену товара'):
        product_price_float = float(PRODUCT_CARD_PAGE.get_product_price().replace('$', ''))

    with allure.step('3) Найдем количество товара'):
        product_qty = PRODUCT_CARD_PAGE.product_qty()

    with allure.step('4) Найдем и кликнем по кнопке Add to cart'):
        PRODUCT_CARD_PAGE.add_to_cart_btn_click()

    with allure.step('5) Найдем новое значение "в корзине"'):
        cart_counter_after = PRODUCT_CARD_PAGE.cart_counter()

    with allure.step('6) Сравним значение каунтера до и после добавления продукта в корзину'):
        assert cart_counter_before != cart_counter_after
        assert cart_counter_after == f"{str(product_qty)} item(s) - ${str(format(product_qty * product_price_float, '.2f'))}"

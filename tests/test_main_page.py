from PageObject.MainPage import MainPage
from PageObject.elements.AlertElement import AlertElement
import allure


@allure.story("Тесты на поиск элементов")
@allure.title("Main page. Проверка наличия элементов на странице")
def test_main_page_elements(browser):
    """
    Тест: Проверка наличия элементов:
    1) продуктовые тумбы - 4 шт
    2) в каждой продуктовой тумбе есть :
    - кнопка Add to cart
    - кнопка Add to wishlist
    - кнопка Compare this product
    3) при клике на "compare this product" появляется блок "Success: You have added #название_продукта to your product comparison!"
    """

    MAIN_PAGE = MainPage(browser)
    MAIN_PAGE.open_(browser.url)

    with allure.step('1)проверка что продуктовых тумбы 4шт'):
        amount_of_tumbs = len(MAIN_PAGE.tumb_list())
        assert amount_of_tumbs == 4

    with allure.step(
            '2)проверка что у каждой тумбы есть кнопки "Add to cart", "Compare this product", "Add to wishlist"'):
        for number in range(amount_of_tumbs):
            assert MAIN_PAGE.add_to_cart_button_is_present(number)
            assert MAIN_PAGE.add_to_wish_list_button_is_present(number)
            assert MAIN_PAGE.add_to_comparison_button_is_present(number)

    for number in range(amount_of_tumbs):
        with allure.step(
                '3)проверка что при клике на "compare this product" появляется блок "Success: You have added #название_продукта to your product comparison!"'):
            product_name = MAIN_PAGE.click_compare_this_product(number)
            with allure.step(f'Продукт {product_name}'):
                assert f"FAILED ON PURPOSE Success: You have added {product_name} to your product comparison!" in AlertElement(
                    browser).comparison_message

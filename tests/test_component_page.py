from PageObject.CatalogPage import CatalogPage
from utils import *
import allure


@allure.story("Тесты на поиск элементов")
@allure.title("Components. Проверка наличия элементов на странице")
def test_catalog_page(browser):
    """
    Тест: Поиск элементов
    1) Поиск и переход в раздел Desktops через блок категорий слева
    2) Поиск заголовка выбранной категориии
    3) Поиск выбранной категории в бредкрамбах
    4) Поиск и выбор подкатегории
    5) Поиск выбранной подкатегории в бредкрамбах
    6) Поиск изображения продукта на продуктовой тумбе
    """

    CATALOG_PAGE = CatalogPage(browser)
    CATALOG_PAGE.open_(browser.url + CATALOG_PATH)

    with allure.step('1) Поиск и переход в раздел Desktops через блок категорий слева'):
        CATALOG_PAGE.navigate_to_Desktops_through_side_bar()

    with allure.step('2) Поиск заголовка выбранной категориии'):
        assert "Desktops" in CATALOG_PAGE.h1_page_title()

    with allure.step('3) Поиск выбранной категории в бредкрамбах'):
        assert "Desktops" in CATALOG_PAGE.first_breadcrumb_text()

    with allure.step('4) Поиск и выбор подкатегории Мак'):
        CATALOG_PAGE.select_subcategory_Mac()

    with allure.step('5) Поиск выбранной подкатегории в бредкрамбах'):
        assert "Mac" in CATALOG_PAGE.second_breadcrumb_text()

    with allure.step('6) Проверить что картинка на карточке товара = iMac'):
        assert CATALOG_PAGE.first_product_img_alt() == "iMac"

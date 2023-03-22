from PageObject.CatalogPage import CatalogPage


def test_CATALOG_PAGE(browser):
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
    CATALOG_PAGE.open(browser.url)

    # 1) Поиск и переход в раздел Desktops через блок категорий слева
    CATALOG_PAGE.navigate_to_Desktops_through_side_bar()

    # 2) Поиск заголовка выбранной категориии
    assert "Desktops" in CATALOG_PAGE.h1_page_title()

    # 3) Поиск выбранной категории в бредкрамбах
    assert "Desktops" in CATALOG_PAGE.first_breadcrumb()

    # 4) Поиск и выбор подкатегории Мак
    CATALOG_PAGE.select_subcategory_Mac()

    # 5) Поиск выбранной подкатегории в бредкрамбах
    assert "Mac" in CATALOG_PAGE.second_breadcrumb()

    # 6) Проверить что картинка на карточке товара = iMac
    assert CATALOG_PAGE.first_product_img_alt() == "iMac"

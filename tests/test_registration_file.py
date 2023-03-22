from selenium.webdriver.common.by import By
from utils import *
from PageObject.RegistartionPage import RegistartionPage


def test_register_page(browser):
    """
    Тест: Поиск элементов
    1) Заголовк "Register Account", проверка цвета и размера его шрифта
    2) Найдем и вводем валидные данные в поля:
    -Firstname,
    -Lastname,
    -E-Mail,
    -Telephone,
    -Password,
    -Password Confirm
    3) Найдем ссылку Privat policy. Кликнем по ней
    4) Найдем заглавие модального окна
    5) Найдем кнопку закрытия модального окна и кликнем по ней
    """

    REGISTRATION_PAGE = RegistartionPage(browser)
    REGISTRATION_PAGE.open(browser.url)

    # 1)проверка заголовка "Register Account" текста, цвета и размера его шрифта
    assert "Register Account" in REGISTRATION_PAGE.h1_title()

    # 2)Найдем и вводем валидные данные в поля firstname, lastname, E-Mail, Telephone, Password, Password Confirm
    REGISTRATION_PAGE.input_firstname(FIRSTNAME_NEW)
    REGISTRATION_PAGE.input_lastname(LASTNAME_NEW)
    REGISTRATION_PAGE.input_email(EMAIL_NEW)
    REGISTRATION_PAGE.input_phone(PHONE_NEW)
    REGISTRATION_PAGE.input_password(PASSWORD)
    REGISTRATION_PAGE.confirm_password(PASSWORD)

    # 3)Откроем Privat policy
    REGISTRATION_PAGE.open_private_policy_modal_window()

    # 4)Проверим заглавие модального окна
    assert "Privacy Policy" in REGISTRATION_PAGE.check_private_policy_modal_window_title()

    # 5)Закроем модальное окно
    REGISTRATION_PAGE.close_private_policy_modal_window()
    assert browser.find_element(By.CSS_SELECTOR, "#modal-agree").get_attribute('style') == "display: none;"

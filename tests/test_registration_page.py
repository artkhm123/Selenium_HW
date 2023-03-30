from selenium.webdriver.common.by import By
from PageObject.RegistartionPage import RegistartionPage
from faker import *
from utils import *
import allure

fake = Factory.create()
FIRSTNAME_NEW = fake.first_name()
LASTNAME_NEW = fake.last_name()
EMAIL_NEW = fake.email()
PHONE_NEW = fake.phone_number()
PASSWORD = f"password{FIRSTNAME_NEW}"


@allure.story("Тесты на поиск элементов")
@allure.title("Registration Page. Проверка наличия элементов на странице")
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
    REGISTRATION_PAGE.open_(browser.url + REG_PAGE_PATH)

    with allure.step('1)проверка заголовка "Register Account" текста, цвета и размера его шрифта'):
        assert "Register Account" in REGISTRATION_PAGE.h1_title()

    with allure.step(
            '2)Найдем и вводем валидные данные в поле firstname'):
        REGISTRATION_PAGE.input_firstname(FIRSTNAME_NEW)
    with allure.step(
            '2)Найдем и вводем валидные данные в поле lastname'):
        REGISTRATION_PAGE.input_lastname(LASTNAME_NEW)
    with allure.step(
            '2)Найдем и вводем валидные данные в поле E-Mail'):
        REGISTRATION_PAGE.input_email(EMAIL_NEW)
    with allure.step(
            '2)Найдем и вводем валидные данные в поле Telephone'):
        REGISTRATION_PAGE.input_phone(PHONE_NEW)
    with allure.step(
            '2)Найдем и вводем валидные данные в поле Password'):
        REGISTRATION_PAGE.input_password(PASSWORD)
    with allure.step(
            '2)Найдем и вводем валидные данные в поле Password Confirm'):
        REGISTRATION_PAGE.confirm_password(PASSWORD)

    with allure.step('3)Откроем Privat policy'):
        REGISTRATION_PAGE.open_private_policy_modal_window()

    with allure.step('4)Проверим заглавие модального окна'):
        assert "Privacy Policy" in REGISTRATION_PAGE.private_policy_modal_window_title()

    with allure.step('5)Закроем модальное окно'):
        REGISTRATION_PAGE.close_private_policy_modal_window()
        assert browser.find_element(By.CSS_SELECTOR, "#modal-agree").get_attribute('style') == "display: none;"

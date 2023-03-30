from PageObject.LoginPage import LoginPage
from utils import *
import allure


@allure.story("Тесты на поиск элементов")
@allure.title("Login Page. Проверка наличия элементов а странице.")
def test_incorrect_login(browser):
    """
    Тест: Поверка наличия элементов
    1) Проверить заголовок "Please enter your login details."
    2) Проверить, что блок о не верных данных "No match for Username and/or Password" - отсутствует
    3) Найдем поле username. введем в него не валидное значение
    4) Найдем поле password. введем в него не валидное значение
    5) Найдем кнопку login. кликнем по ней
    6) Блок о не верных данных "No match for Username and/or Password" - появился
    """

    LOGIN_PAGE = LoginPage(browser)
    LOGIN_PAGE.open_(browser.url + LOGIN_PAGE_PATH)

    with allure.step('1) Проверить заголовок "Please enter your login details."'):
        assert "Please enter your login details." in LOGIN_PAGE.h1_page_title()

    with allure.step('2) Проверить, что блок о не верных данных "No match for Username and/or Password" - отсутствует'):
        assert not LOGIN_PAGE.wrong_userdata_message_is_present()

    with allure.step('3) Найдем поле username. введем в него не валидное значение'):
        LOGIN_PAGE.input_username(NON_EXISTING_USERNAME)

    with allure.step('4) Найдем поле password. введем в него не валидное значение'):
        LOGIN_PAGE.input_password(WRONG_PASSWORD)

    with allure.step('5) Найдем кнопку login. кликнем по ней'):
        LOGIN_PAGE.login()

    with allure.step('6) Блок о не верных данных "No match for Username and/or Password" - появился'):
        assert LOGIN_PAGE.wrong_userdata_message_is_present()
        assert "No match for Username and/or Password." in LOGIN_PAGE.wrong_userdata_message()

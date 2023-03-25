from selenium.webdriver.common.by import By

from PageObject.RegistartionPage import RegistartionPage
from PageObject.AccountSuccessPage import AccountSuccessPage
from faker import *

fake = Factory.create()
FIRSTNAME_NEW = fake.first_name()
LASTNAME_NEW = fake.last_name()
EMAIL_NEW = fake.email()
PHONE_NEW = fake.phone_number()
PASSWORD = f"password{FIRSTNAME_NEW}"


def test_register_page(browser):
    """
    1) Зайти на страницу Регистрации
    2) Найдем и вводем валидные данные нового пользователя в поля:
    -Firstname,
    -Lastname,
    -E-Mail,
    -Telephone,
    -Password,
    -Password Confirm
    3) Подтветдим согласие с Privat policy
    4) Завершим регистрацию
    """

    REGISTRATION_PAGE = RegistartionPage(browser)
    REGISTRATION_PAGE.open(browser.url)

    # 1)
    assert "Register Account" in REGISTRATION_PAGE.h1_title()

    # 2)
    REGISTRATION_PAGE.input_firstname(FIRSTNAME_NEW)
    REGISTRATION_PAGE.input_lastname(LASTNAME_NEW)
    REGISTRATION_PAGE.input_email(EMAIL_NEW)
    REGISTRATION_PAGE.input_phone(PHONE_NEW)
    REGISTRATION_PAGE.input_password(PASSWORD)
    REGISTRATION_PAGE.confirm_password(PASSWORD)

    # 3)Подтветдим согласие с Privat policy
    REGISTRATION_PAGE.confirm_private_policy_agreement()

    # 4)Завершим регистрацию
    REGISTRATION_PAGE.confirm_registration()
    assert "Your Account Has Been Created!" in AccountSuccessPage(browser).h1_title()

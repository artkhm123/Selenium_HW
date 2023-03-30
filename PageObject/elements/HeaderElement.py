import time
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class HeaderElement(BasePage):
    CURRENCY_BTN = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")
    USD = (By.CSS_SELECTOR, "button[name='USD']")
    EUR = (By.CSS_SELECTOR, "button[name='EUR']")
    GBP = (By.CSS_SELECTOR, "button[name='GBP']")
    LOGOUT_FROM_ADMIN_PAGE = (By.CSS_SELECTOR, "#header > div > ul > li:nth-child(2) > a > span")
    USER_DDROPDOWN = (By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a")

    def __init__(self, driver):
        super().__init__(driver=driver)

    # @property
    # def change_currency_btn(self):
    #     return self.element(self.CURRENCY_BTN)

    @property
    def choose_USD(self):
        return self.element(self.USD)

    def change_currency_to(self, currency: str):
        time.sleep(1)
        self.element(self.CURRENCY_BTN).click()
        time.sleep(1)
        if currency == "USD":
            self.element(self.USD).click()
        if currency == "EUR":
            self.element(self.EUR).click()
        if currency == "GBP":
            self.element(self.GBP).click()

    def logout_from_admin_page(self):
        return self.element(self.LOGOUT_FROM_ADMIN_PAGE)

    @property
    def user_name(self):
        return self.element(self.USER_DDROPDOWN).text

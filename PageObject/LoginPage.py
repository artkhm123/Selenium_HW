from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(BasePage):
    LOGIN_PAGE_PATH = "/admin"
    CONTENT = (By.CSS_SELECTOR, "#content")
    H1_TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    USERDATA_ALLERT = (By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type=submit]")

    def open(self, base_url):
        self.driver.get(base_url + self.LOGIN_PAGE_PATH)
        WebDriverWait(self.driver, self.default_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def h1_page_title(self):
        return self.element(self.H1_TITLE).text

    def wrong_userdata_message(self):
        return self.element(self.USERDATA_ALLERT).text

    def wrong_userdata_message_is_present(self):
        # элемент по дефолту отсутствует
        if len(self.driver.find_elements(*self.USERDATA_ALLERT)) == 0:
            return False
        else:
            return True

    def input_username(self, text):
        self.element(self.USERNAME).clear()
        self.element(self.USERNAME).send_keys(text)

    def input_password(self, text):
        self.element(self.PASSWORD).clear()
        self.element(self.PASSWORD).send_keys(text)

    def login(self):
        self.element(self.BUTTON_LOGIN).click()
        time.sleep(0.5)

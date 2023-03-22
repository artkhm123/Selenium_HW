from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegistartionPage(BasePage):
    REG_PAGE_PATH = "/index.php?route=account/register"
    H1_TITLE = (By.CSS_SELECTOR, "#content > h1")
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    ACCOUNT_FRAIM = (By.CSS_SELECTOR, "#account-register")
    MODAL_TITLE = (By.CSS_SELECTOR, "h4.modal-title")
    CLOSE_BTN = (By.CSS_SELECTOR, "button.close")

    def open(self, base_url):
        self.driver.get(base_url + self.REG_PAGE_PATH)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def h1_title(self):
        return self.element(self.H1_TITLE).text

    def check_title_font_color(self):
        return self.driver.element(self.H1_TITLE).value_of_css_property("color")

    def check_title_font_color(self):
        title = self.element(self.H1_TITLE).text
        return int(title.value_of_css_property("font-size").replace('px', ''))

    def input_firstname(self, text):
        self.element(self.FIRSTNAME).clear()
        self.element(self.FIRSTNAME).send_keys(text)

    def input_lastname(self, text):
        self.element(self.LASTNAME).clear()
        self.element(self.LASTNAME).send_keys(text)

    def input_email(self, text):
        self.element(self.EMAIL).clear()
        self.element(self.EMAIL).send_keys(text)

    def input_phone(self, text):
        self.element(self.TELEPHONE).clear()
        self.element(self.TELEPHONE).send_keys(text)

    def input_password(self, text):
        self.element(self.PASSWORD).clear()
        self.element(self.PASSWORD).send_keys(text)

    def confirm_password(self, text):
        self.element(self.PASSWORD_CONFIRM).clear()
        self.element(self.PASSWORD_CONFIRM).send_keys(text)

    def open_private_policy_modal_window(self):
        account_reg_form = self.element(self.ACCOUNT_FRAIM)
        account_reg_form.find_element(By.LINK_TEXT, "Privacy Policy").click()

    def check_private_policy_modal_window_title(self):
        # WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
        return self.element(self.MODAL_TITLE).text

    def close_private_policy_modal_window(self):
        self.element(self.CLOSE_BTN).click()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body[class='']")))

import time
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class AlertElement(BasePage):
    ALLERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    @property
    def comparison_message(self):
        time.sleep(0.5)
        return self.get_text(self.ALLERT_SUCCESS)

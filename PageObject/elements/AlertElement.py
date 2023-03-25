import time
from selenium.webdriver.common.by import By

from PageObject.elements.BaseElement import BaseElement


class AlertElement(BaseElement):
    ALLERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    @property
    def comparison_message(self):
        time.sleep(1)
        return self.element(self.ALLERT_SUCCESS).text

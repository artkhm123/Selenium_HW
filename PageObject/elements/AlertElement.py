import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:

    def __init__(self, driver):
        self.driver = driver

    @property
    def comparison_message(self):
        time.sleep(1)
        # WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        return self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

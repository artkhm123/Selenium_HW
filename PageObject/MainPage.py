from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    TUMB_LIST = (By.CSS_SELECTOR, ".product-thumb.transition")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[onclick*='cart']")
    ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, "button[onclick*='wishlist']")
    CAMPARE_BTN = (By.CSS_SELECTOR, "button[onclick*='compare']")

    def open(self, base_url):
        self.driver.get(base_url)
        WebDriverWait(self.driver, self.default_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def tumb_list(self):
        return self.elements(self.TUMB_LIST)

    def tumb(self, tumb_number):
        return self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb.transition")[tumb_number]

    def add_to_cart_button_is_present(self, tumb_number):
        if len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='cart']")) > 0:
            return True
        else:
            return False

    def add_to_wish_list_button_is_present(self, tumb_number):
        if len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='wishlist']")) > 0:
            return True
        else:
            return False

    def add_to_comparison_button_is_present(self, tumb_number):
        if len(self.tumb(tumb_number).find_elements(By.CSS_SELECTOR, "button[onclick*='compare']")) > 0:
            return True
        else:
            return False

    def click_compare_this_product(self, tumb_number):
        product_name = self.tumb(tumb_number).find_element(By.CSS_SELECTOR, ".caption h4 a").text
        self.tumb(tumb_number).find_element(By.CSS_SELECTOR, "button[onclick*='compare']").click()
        return product_name

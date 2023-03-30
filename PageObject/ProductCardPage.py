from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductCardPage(BasePage):
    iPHONE_PAGE = "/iphone"
    MAC_PAGE = "/macbook"

    CART_COUNTER = (By.CSS_SELECTOR, "#cart-total")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    PRODUCT_QTY = (By.CSS_SELECTOR, "#input-quantity")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_CART_BTN2 = (By.CSS_SELECTOR, "button[onclick*='cart']")

    def open(self, base_url):
        self.driver.get(base_url)
        WebDriverWait(self.driver, self.default_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def cart_counter(self):
        return self.element(self.CART_COUNTER).text

    def get_product_price(self):
        return self.element(self.PRODUCT_PRICE).text

    def product_qty(self):
        return int(self.element(self.PRODUCT_QTY).get_attribute("value"))

    def add_to_cart_btn_click(self):
        self.element(self.ADD_TO_CART_BTN).click()
        time.sleep(0.5)

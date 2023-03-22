from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CatalogPage(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumb > li")
    H2_TITLE = (By.CSS_SELECTOR, "h2")
    SIDE_BAR = (By.CSS_SELECTOR, "#column-left")
    MAC_SUBCATEGORY = (By.CSS_SELECTOR, f"#column-left > div > a[href='http://192.168.31.28:8081/desktops/mac']")
    PRODUCT_TUMB = (By.CSS_SELECTOR, ".product-thumb")
    IMG = (By.TAG_NAME, "img")
    CATALOG_PATH = "/component"

    def open(self, base_url):
        self.driver.get(base_url + self.CATALOG_PATH)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    def navigate_to_Desktops_through_side_bar(self):
        aside_block = self.element(self.SIDE_BAR)
        aside_block.find_element(By.PARTIAL_LINK_TEXT, "Desktops").click()

    def h1_page_title(self):
        return self.element(self.H2_TITLE).text

    def first_breadcrumb(self):
        return self.elements(self.BREADCRUMBS)[1].text

    def select_subcategory_Mac(self):
        self.element(self.MAC_SUBCATEGORY).click()

    def second_breadcrumb(self):
        return self.elements(self.BREADCRUMBS)[2].text

    def first_product(self):
        return self.elements(self.PRODUCT_TUMB)[0]

    def first_product_img_alt(self):
        return (self.first_product().find_element(*self.IMG)).get_attribute("alt")

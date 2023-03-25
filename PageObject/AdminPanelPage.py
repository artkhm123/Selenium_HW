from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminMainPage(BasePage):
    SIDE_MENU = (By.CSS_SELECTOR, "#menu")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    CATALOG_PRODUCTS = (By.CSS_SELECTOR, "#menu-catalog > #collapse1 > li:nth-child(2)")
    H1_TITLE = (By.CSS_SELECTOR, "#content > div.page-header > div > h1")
    ADD_BTN = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    GENERAL_TAB = (By.LINK_TEXT, "General")
    DATA_TAB = (By.LINK_TEXT, "Data")
    LINKS_TAB = (By.LINK_TEXT, "Links")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    PRODUCT_METADATA_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    PRODUCT_PRICE_INPUT = (By.CSS_SELECTOR, "#input-price")
    PRODUCT_QTY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    SAVE_BTN = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    FILTER_BY_NAME_INPUT = (By.CSS_SELECTOR, "#input-name")
    FILTER_SUBMIT = (By.CSS_SELECTOR, "#button-filter > i")
    SEARCHED_PRODUCT_NAME = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[3]")
    SEARCHED_PRODUCT_MODEL = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[4]")
    SEARCHED_PRODUCT_PRICE = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[5]")
    SEARCHED_PRODUCT_QTY = (By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[6]/span")
    FILTER_PANEL = (By.CSS_SELECTOR, "#filter-product > div > div.panel-heading")
    FILTERED_PRODUCT_CHECKBOX = (
        By.CSS_SELECTOR, "#form-product > div > table > tbody > tr > td:nth-child(1) > input[type=checkbox]")
    RESULT_LIST = (By.CSS_SELECTOR, "#form-product > div > table > tbody")
    DELETE_BTN = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    NO_RESULT_TEXT = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr > td")

    @property
    def h1_page_title(self):
        return self.element(self.H1_TITLE).text

    def side_menu_catalog(self):
        return self.element(self.MENU_CATALOG)

    def menu_products(self):
        return self.element(self.CATALOG_PRODUCTS)

    def add_product_btn(self):
        return self.element(self.ADD_BTN)

    def save_product_btn(self):
        return self.element(self.SAVE_BTN)

    def input_product_name(self, text):
        self.element(self.PRODUCT_NAME_INPUT).clear()
        self.element(self.PRODUCT_NAME_INPUT).send_keys(text)

    def input_meta_tag_title(self, text):
        self.element(self.PRODUCT_METADATA_INPUT).clear()
        self.element(self.PRODUCT_METADATA_INPUT).send_keys(text)

    def switch_tab_to(self, tab: str):
        if tab.strip().upper() == "GENERAL":
            self.element(self.GENERAL_TAB).click()
        if tab.strip().upper() == "DATA":
            self.element(self.DATA_TAB).click()
        if tab.strip().upper() == "LINKS":
            self.element(self.LINKS_TAB).click()
        # else:
        #     raise AssertionError(f"Не смог переключиться на табу {tab}")

    def input_product_model(self, text):
        self.element(self.PRODUCT_MODEL_INPUT).clear()
        self.element(self.PRODUCT_MODEL_INPUT).send_keys(text)

    def input_product_price(self, text):
        self.element(self.PRODUCT_PRICE_INPUT).clear()
        self.element(self.PRODUCT_PRICE_INPUT).send_keys(text)

    def input_product_qty(self, text):
        self.element(self.PRODUCT_QTY_INPUT).clear()
        self.element(self.PRODUCT_QTY_INPUT).send_keys(text)

    def filter_by_product_name(self, text):
        self.element(self.FILTER_BY_NAME_INPUT).click()
        self.element(self.FILTER_BY_NAME_INPUT).clear()
        self.element(self.FILTER_BY_NAME_INPUT).send_keys(text)
        self.element(self.FILTER_PANEL).click()

    def filter_submit_btn(self):
        js_code = "document.querySelector('#button-filter').click();"
        self.driver.execute_script(js_code)

    @property
    def search_result(self):
        result_dict = {
            "name": self.element(self.SEARCHED_PRODUCT_NAME).text,
            "model": self.element(self.SEARCHED_PRODUCT_MODEL).text,
            "price": self.element(self.SEARCHED_PRODUCT_PRICE).text,
            "qty": self.element(self.SEARCHED_PRODUCT_QTY).text
        }
        return result_dict

    def select_filtered_product(self):
        self.element(self.FILTERED_PRODUCT_CHECKBOX).click()

    def delete_product(self):
        self.element(self.DELETE_BTN).click()
        alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert.accept()

    def no_results_is_present(self):
        return self.element(self.RESULT_LIST).find_element(*self.NO_RESULT_TEXT).text

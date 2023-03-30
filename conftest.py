import os
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions




def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices = ["chrome", "ff", "firefox", "yandex", "ya", "edge"])
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("~\\khomiakov_a\\Desktop\\Python\\drivers\\"))
    parser.addoption("--url", action="store", default="http://192.168.31.28:8081")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    _drivers_path = request.config.getoption("--drivers")
    _url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    driver = None
    if _browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.headless = headless
        service = ChromeService(executable_path=_drivers_path + "chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif _browser == "ff" or _browser == "firefox":
        ff_options = FFOptions()
        ff_options.headless = headless
        service = FFService(executable_path=_drivers_path + "geckodriver")
        driver = webdriver.Firefox(service=service, options=ff_options)
    elif _browser == "yandex" or _browser == "ya":
        ya_options = ChromeOptions()
        ya_options.headless = headless
        service = ChromeService(executable_path=_drivers_path + "yandexdriver")
        driver = webdriver.Chrome(service=service, options=ya_options)
    elif _browser == "edge":
        edge_options = EdgeOptions()
        edge_options.headless = headless
        service = EdgeService(executable_path=_drivers_path + "msedgedriver")
        driver = webdriver.Edge(service=service, options=edge_options)
    driver.get(_url)
    driver.url = _url
    driver.maximize_window()
    yield driver
    driver.quit()

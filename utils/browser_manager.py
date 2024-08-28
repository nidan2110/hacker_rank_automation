from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    def __init__(self, browser="chrome"):
        self.browser = browser

    def get_driver(self):
        if self.browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-extensions")

            # Use WebDriverManager to automatically download and manage ChromeDriver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            return driver
        else:
            raise ValueError(f"Browser '{self.browser}' is not supported.")

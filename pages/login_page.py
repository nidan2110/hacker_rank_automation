from selenium.webdriver.common.by import By
from config.config import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL + "/login"
        self.username_field = (By.ID, "input-username")
        self.password_field = (By.ID, "input-password")
        self.login_button = (By.ID, "btn-login")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)

    @allure.step("Entering username: {username}")
    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Clicking the login button")
    def click_login(self):
        self.driver.find_element(By.ID, "submit").click()

    def get_success_message(self):
        # Wait until the success message is visible
        success = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        return success.text

    def get_error_message(self):
        # Wait until the error message is visible
        error = self.wait.until(
            EC.visibility_of_element_located((By.ID, "error"))
        )
        return error.text

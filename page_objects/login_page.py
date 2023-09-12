from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    __url = "https://login-app-iota.vercel.app/"
    __username_field = (By.ID, 'username_textbox')
    __password_field = (By.ID, 'password_textbox')
    __submit_button = (By.XPATH, "//button[@type='submit']")
    __error_label_field = (By.XPATH, "//div[text()='Invalid Credentials']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_login(self, username, password):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__username_field))
        username_data = self._driver.find_element(*self.__username_field)
        password_data = self._driver.find_element(*self.__password_field)
        submit_button_field = self._driver.find_element(*self.__submit_button)

        username_data.send_keys(username)
        password_data.send_keys(password)

        submit_button_field.click()

    def error_label_text(self):
        error_label = self._driver.find_element(*self.__error_label_field)
        actual_text = error_label.text
        return actual_text

    def is_error_label_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__error_label_field))
        self._driver.find_element(*self.__error_label_field).is_displayed()

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage:
    __login_url = "https://login-app-iota.vercel.app/login"
    __about_url = "https://login-app-iota.vercel.app/about"
    __about_menu_link = (By.XPATH, "//*[@id='navbarSupportedContent']/div/a[5]")
    __logout_btn = (By.LINK_TEXT, "Logout")

    __header_text = (By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def current_url(self):
        return self._driver.current_url

    def open_about_page(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__about_menu_link))
        about_link = self._driver.find_element(*self.__about_menu_link)
        about_link.click()
        current_url = self._driver.current_url
        expected_url = self.__about_url
        assert current_url == expected_url

    def header_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__header_text))
        header = self._driver.find_element(*self.__header_text)
        assert header.is_displayed(), "Welcome message not displayed"
        actual_text = header.text
        assert actual_text == "Welcome to Selenium Learning Group", "Welcome text does not match"

    def perform_logout(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__logout_btn))
        logout = self._driver.find_element(*self.__logout_btn)
        logout.click()
        login_url = self.__login_url
        assert login_url == "https://login-app-iota.vercel.app/login"

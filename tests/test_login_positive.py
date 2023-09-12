# import required packages
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage

service = ChromeService(executable_path=ChromeDriverManager().install())


@pytest.mark.login
@pytest.mark.login_positive
@pytest.mark.parametrize("username,password", [("admin", "admin123")])
def test_valid_user_login(driver, username, password):
    """Test :A user with valid credentials should be able to Log in successfully
    URL :https://login-app-iota.vercel.app
    """
    # Act
    # Navigate to Site URL and perform login and Validate if the default URL is pointing to the login route
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

    # Validate logged in URL

    loaded_url = dashboard_page.current_url()
    assert loaded_url == "https://login-app-iota.vercel.app/dashboard", "Default logged URL route should be dashboard"

    # Assert
    # Validate header title
    dashboard_page.open_about_page()
    dashboard_page.header_text_is_displayed()

    # locate logout button
    # click on logout button
    # validate that login page URL is displayed
    dashboard_page.perform_logout()

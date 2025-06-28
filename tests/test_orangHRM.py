from time import sleep

from pages.login_page import LoginPage


def test_login(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")


    sleep(3)

def test_login_with_wrong_credentials(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    login_page.login("Admin", "admin1234")
    assert login_page.error_message() == "Invalid credentials"
import allure
from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
    """
        # Locators
        self.user_name = "Admin"
        self.password = "admin123"
        self.selectors = {
            "username_locator": '//input[@name="username"]',
            "password_locator": '//input[@name="password"]',
            "loginBtn": '//button[@type="submit"]',
            "adminIcon": '//a[@href="/web/index.php/admin/viewAdminModule"]'
        }
"""


    def enter_username(self, username):
        self.page.locator("input[name='username']").fill(username)

    def enter_password(self, password):
        self.page.locator("input[name='password']").fill(password)

    def click_login(self):
        self.page.locator("button[type='submit']").click()

    def error_message(self):
        return self.page.locator("p.oxd-alert-content-text").text_content()

    @allure.step("Login with username: {username} and password: {password}")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
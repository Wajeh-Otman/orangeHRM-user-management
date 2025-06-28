import allure
from playwright.sync_api import Page

class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        self.page.locator('.oxd-userdropdown').click()
        self.page.locator('[href="/web/index.php/auth/logout"]').click()


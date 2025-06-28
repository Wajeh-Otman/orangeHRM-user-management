import allure
from playwright.sync_api import Page

class AdminUserManagement:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Click on Add User button")
    def click_add_user_btn(self):
        self.page.get_by_text(" Add ").click()
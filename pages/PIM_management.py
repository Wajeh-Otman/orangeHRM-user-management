import allure
from playwright.sync_api import Page

class PIMManagement:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Click on Add button")
    def click_add_employee_btn(self):
        self.page.locator(".oxd-button--secondary").nth(1).click()
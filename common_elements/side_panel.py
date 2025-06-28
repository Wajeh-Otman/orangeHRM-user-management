import allure
from playwright.sync_api import Page

class SidePanel:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Click on {page_name} page")
    def move_to(self, page_name):
        self.page.locator(".oxd-main-menu-item--name", has_text=page_name).click()
import allure
from playwright.sync_api import Page


class NewUser:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Select role: {role}")
    def select_role(self, role:str):
        self.page.locator(".oxd-select-text--arrow").nth(0).click()
        self.page.locator("[role='listbox'] .oxd-select-option", has_text=role).click()

    @allure.step("Select status: {status}")
    def select_status(self, status:str):
        self.page.locator(".oxd-select-text--arrow").nth(1).click()
        self.page.locator("[role='listbox'] .oxd-select-option", has_text=status).click()

    @allure.step("Select employee name: {selected_value}")
    def select_employee_name(self, regex:str, selected_value:str):
        self.page.locator('[placeholder="Type for hints..."]').fill(regex)
        self.page.locator("").fill(selected_value)

    @allure.step("Enter username")
    def select_username(self, username: str):
        self.page.locator('[fdprocessedid="w5hq5"]').fill(username)

    @allure.step("Enter password {password}")
    def enter_password(self, password: str):
        self.page.locator('[type="password"]').nth(0).fill(password)

    @allure.step("Enter confirm {password}")
    def enter_confirm_password(self, password: str):
        self.page.locator('[type="password"]').nth(1).fill(password)

    @allure.step("Click on cancel button")
    def click_on_cancel_btn(self):
        self.page.locator(".oxd-button--ghost").click()

    @allure.step("Click on save button")
    def click_on_save_btn(self):
        self.page.locator('[type="submit"]').click()

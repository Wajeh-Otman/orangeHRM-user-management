import allure
from playwright.sync_api import Page


class NewEmployee:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Enter first name {username}")
    def enter_first_name(self, username: str):
        self.page.locator('[placeholder="First Name"]').fill(username)

    @allure.step("Enter middle name {username}")
    def enter_middle_name(self, username: str):
        self.page.locator('[placeholder="Middle Name"]').fill(username)

    @allure.step("Enter last name {username}")
    def enter_last_name(self, username: str):
        self.page.locator('[placeholder="Last Name"]').fill(username)

    @allure.step("click on create login details")
    def create_login_details(self):
        self.page.locator(".oxd-switch-input--active").click()

    @allure.step("Enter username {username}")
    def enter_username(self, username: str):
        self.page.locator('.oxd-input.oxd-input--active').nth(5).fill(username)

    @allure.step("Select enable")
    def select_enable(self):
        self.page.locator(".oxd-radio-input--active").nth(0).click()

    @allure.step("Select disable")
    def select_disable(self):
        self.page.locator(".oxd-radio-input--active").nth(1).click()

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




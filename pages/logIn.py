
class Login:

    def __init__(self):
        # Locators
        self.user_name = "Admin"
        self.password = "admin123"
        self.selectors = {
            "username_locator": '//input[@name="username"]',
            "password_locator": '//input[@name="password"]',
            "loginBtn": '//button[@type="submit"]',
            "adminIcon": '//a[@href="/web/index.php/admin/viewAdminModule"]'

        }


    def login(self,page):
        page.wait_for_selector(self.selectors["username_locator"]).type(self.user_name)
        page.wait_for_selector(self.selectors["password_locator"]).type(self.password)
        page.wait_for_selector(self.selectors["loginBtn"]).click()
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors["adminIcon"]).click()

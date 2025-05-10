
class adminPage:

    def __init__(self):
        # Locators
        self.selectors = {
            "addBtn": '//button[text()=" Add "]',
            "username_locator": "//label[text()='Username']/following::input[1]",
            "userRole_locator": "(//div[@class='oxd-select-text-input'])[1]",
            "userRole_value":"//div[@role='option' and contains(., 'ESS')]",
            "empName_locator": "//input[@placeholder='Type for hints...']",
            "empName_value": "//div[@role='listbox']//span",
            "status_locator": "(//div[@class='oxd-select-text-input'])[2]",
            "status_value": "//div[@role='option' and contains(., 'Enable')]",
            "searchBtn": '//button[@type="submit"]',
            "resetBtn": '//button[text()=" Reset "]'

        }

    def goToAddUserPage(self,page):
        page.wait_for_selector(self.selectors['addBtn']).click()
        page.wait_for_timeout(3000)

    def searchByUsername(self,page):
        page.locator(self.selectors["username_locator"]).fill("admin")
        page.wait_for_selector(self.selectors['searchBtn']).click()
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors['resetBtn']).click()
        page.wait_for_timeout(3000)


    def searchByUserRole(self,page):
        page.wait_for_selector(self.selectors["userRole_locator"]).click()
        page.wait_for_selector(self.selectors["userRole_value"]).click()
        page.wait_for_selector(self.selectors['searchBtn']).click()
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors['resetBtn']).click()
        page.wait_for_timeout(3000)

    def searchByEmpName(self, page):
        page.wait_for_selector(self.selectors["empName_locator"]).fill("a")
        page.locator(self.selectors["empName_value"]).first.click()
        page.wait_for_selector(self.selectors['searchBtn']).click()
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors['resetBtn']).click()
        page.wait_for_timeout(3000)

    def searchByStatus(self, page):
        page.query_selector(self.selectors["status_locator"]).click()
        page.wait_for_selector(self.selectors["status_value"]).click()
        page.wait_for_selector(self.selectors['searchBtn']).click()
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors['resetBtn']).click()
        page.wait_for_timeout(3000)

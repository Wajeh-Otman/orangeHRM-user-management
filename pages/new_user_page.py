class addUser:

    def __init__(self):
        # Locators
        self.selectors = {
            "addBtn": '//button[text()=" Add "]',
            "userRole_locator": "(//div[@class='oxd-select-text-input'])[1]",
            "userRole_value": "//div[@role='option' and contains(., 'ESS')]",
            "status_locator": "(//div[@class='oxd-select-text-input'])[2]",
            "status_value": "//div[@role='option' and contains(., 'Enable')]",
            "empName_locator": "//input[@placeholder='Type for hints...']",
            "empName_value": "//div[@role='listbox']//span",
            "userName_locator": '(//input[@autocomplete="off"])[1]',
            "password_locator": '(//input[@type="password"])[1]',
            "confirmPassword_locator": '(//input[@type="password"])[2]',
            "saveBtn": '//button[@type="submit"]'
        }


    def addUser(self,page):
        page.wait_for_selector(self.selectors['addBtn']).click()
        page.locator(self.selectors['userRole_locator']).click()
        page.wait_for_selector(self.selectors['userRole_value']).click()
        page.locator(self.selectors["status_locator"]).click()
        page.wait_for_selector(self.selectors["status_value"]).click()
        page.locator(self.selectors['empName_locator']).fill("b")
        page.locator(self.selectors['empName_value']).first.click()
        page.wait_for_selector(self.selectors['userName_locator']).type("John John")
        page.wait_for_selector(self.selectors['password_locator']).type("a1234567")
        page.wait_for_selector(self.selectors['confirmPassword_locator']).type("a1234567")
        page.wait_for_selector(self.selectors['saveBtn']).click()
        page.wait_for_timeout(7000)
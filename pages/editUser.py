class editUser:

    def __init__(self):
        # Locators
        self.selectors = {
            "editBtn": '(//button[@type="button"]//i[@class="oxd-icon bi-pencil-fill"])[2]',
            "userRole_locator": '(//div[@tabindex="0"])[1]',
            "userRole_value": "//div[@role='option' and contains(., 'ESS')]",
            "status_locator": '(//div[@tabindex="0"])[2]',
            "status_value": "//div[@role='option' and contains(., 'Enable')]",
            "empName_locator": '//input[@placeholder="Type for hints..."]',
            "empName_value": "//div[@role='listbox']//span",
            "username_locator": '//input[@autocomplete="off"]',
            "changePasswordBtn": '//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]',
            "password": '(//input[@type="password"])[1]',
            "confPassword": '(//input[@type="password"])[2]',
            "saveBtn": '//button[@type="submit"]',
            "cancelBtn": '//button[text()=" Cancel "]]'

        }
    def selectUser(self, page):
        page.wait_for_selector(self.selectors['editBtn']).click()
        page.wait_for_timeout(2000)

    def editUser(self, page):

        page.locator(self.selectors['userRole_locator']).click()
        page.wait_for_selector(self.selectors['userRole_value']).click()
        page.locator(self.selectors['status_locator']).click()
        page.wait_for_selector(self.selectors['status_value']).click()
        page.wait_for_selector(self.selectors['empName_locator']).fill('e')
        page.wait_for_timeout(3000)
        page.locator(self.selectors['empName_value']).first.click()
        page.wait_for_selector(self.selectors['username_locator']).fill('asd')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['username_locator']).fill('username11')

        page.wait_for_selector(self.selectors['changePasswordBtn']).click()
        page.wait_for_selector(self.selectors['password']).fill('1234567')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['password']).fill('asdfghj')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['password']).fill('12wsd')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['password']).fill('a1234567')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['confPassword']).fill('b1234567')
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['confPassword']).fill('a1234567')
        page.wait_for_timeout(3000)
        page.wait_for_selector(self.selectors['saveBtn']).click()
        page.wait_for_timeout(7000)

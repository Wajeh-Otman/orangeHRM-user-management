class deleteUser:


    def __init__(self):
        # Locators
        self.selectors = {
            "deleteSingleBtn": '(//button[@type="button"]//i[@class="oxd-icon bi-trash"])[2]',
            "confirmBtn": '//button[text()=" Yes, Delete "]',
            "cancelBtn": '//button[text()=" Yes, Delete "]',
            "selectAllBtn": "//div[@class='oxd-table-header']//span[contains(@class, 'oxd-checkbox-input')]",
            "selectFirstUser": "(//div[@class='oxd-table-card']//span[contains(@class, 'oxd-checkbox-input')])[2]",
            "selectSecondUser": "(//div[@class='oxd-table-card']//span[contains(@class, 'oxd-checkbox-input')])[3]",

            "deleteBtn": '//button[text()=" Delete Selected "]',


        }

    def deleteSingleUser(self,page):
        page.wait_for_selector(self.selectors['deleteSingleBtn']).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector(self.selectors['cancelBtn']).click()
        page.wait_for_selector(self.selectors['deleteSingleBtn']).click()
        page.wait_for_timeout(1000)
        page.wait_for_selector(self.selectors['confirmBtn']).click()
        page.wait_for_timeout(5000)


    def deleteMultiUsers(self, page):
        page.locator(self.selectors['selectAllBtn']).click()
        page.wait_for_timeout(2000)
        page.locator(self.selectors['selectAllBtn']).click()
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['selectFirstUser']).click()
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['selectSecondUser']).click()
        page.wait_for_selector(self.selectors['deleteBtn']).click()
        page.wait_for_timeout(2000)
        page.wait_for_selector(self.selectors['confirmBtn']).click()
        page.wait_for_timeout(5000)
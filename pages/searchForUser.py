
class searchForUserPage:

    def __init__(self):
        # Locators
        self.selectors = {
            "username_locator": '//input[@name="username"]',
            "password_locator": '//input[@name="password"]',
            "loginBtn": '//button[@type="submit"]',
            "adminIcon": '//a[@href="/web/index.php/admin/viewAdminModule"]'

        }


""" page.locator("//label[text()='Username']/following::input[1]").fill("john john")
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.wait_for_selector('//button[text()=" Reset "]').click()


    page.wait_for_selector("(//div[@class='oxd-select-text-input'])[1]").click()
    page.wait_for_selector("//div[@role='option' and contains(., 'ESS')]").click()
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.wait_for_selector('//button[text()=" Reset "]').click()

#######    search by Employee Name   #######
    # empName = page.wait_for_selector("//input[@placeholder='Type for hints...']")
    # empName.fill("aa")
    # page.locator("//div[@role='listbox']//span").first.click()
    # page.wait_for_selector('//button[@type="submit"]').click()
    # page.wait_for_timeout(3000)
    # page.wait_for_selector('//button[text()=" Reset "]').click()


    page.query_selector("(//div[@class='oxd-select-text-input'])[2]").click()
    page.wait_for_selector("//div[@role='option' and contains(., 'Enable')]").click()
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.wait_for_selector('//button[text()=" Reset "]').click()


    def searchByUsername(self,page):
        page.wait_for_timeout(3000)
        
    def searchByUserRole(self,page):
        page.wait_for_timeout(3000)
        
    def searchByEmpName(self,page):
        page.wait_for_timeout(3000)
        
    def searchByStatus(self,page):
        page.wait_for_timeout(3000)
    """
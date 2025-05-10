from playwright.sync_api import sync_playwright
from pages import addUser
from pages import logIn
from pages import adminMainPage
from pages import editUser
from pages import deleteUserPage


def init_browser(url):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # Store references to close everything later
    page.playwright = playwright
    return page



if __name__ == '__main__':
    page = init_browser('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login_page = logIn.Login()
    addUserPage = addUser.addUser()
    admin_Page = adminMainPage.adminPage()
    edit_user = editUser.editUser()
    del_user = deleteUserPage.deleteUser()
    login_page.login(page)
    page.wait_for_timeout(3000)

    # addUserPage.addUser(page)
    #
    # admin_Page.searchByUsername(page)
    # admin_Page.searchByUserRole(page)
    # admin_Page.searchByEmpName(page)
    # admin_Page.searchByStatus(page)
    #
    # edit_user.selectUser(page)
    # edit_user.editUser(page)
    #
    del_user.deleteSingleUser(page)
    # del_user.deleteMultiUsers(page)

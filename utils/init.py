from playwright.sync_api import sync_playwright
from pages import add_User
from pages import logIn


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
    login_page=logIn.LoginPage()
    addUserPage =add_User.addUserPage()
    login_page.login(page)
    page.wait_for_timeout(3000)

    addUserPage.addUser(page)

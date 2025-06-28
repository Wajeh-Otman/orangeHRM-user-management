from playwright.sync_api import Playwright


class BrowserHandler:

    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.browser = None


    def init_browser(self):
        self.browser = self.playwright.chromium.launch(headless=False)
        context = self.browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("browser is ready")
        return page

    def close_browser(self):
        self.browser.close()
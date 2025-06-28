import allure
import pytest
from playwright.sync_api import Playwright

from utils.BrowserHandler import BrowserHandler


@pytest.fixture(scope="function")
def browser_config(playwright: Playwright):
    browser_handler = BrowserHandler(playwright)

    page = browser_handler.init_browser()
    yield page
    browser_handler.close_browser()
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("browser_config")
        if page is not None:
            screenshot =page.screenshot(path=f"screenshots/{item.name}.png")
            allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
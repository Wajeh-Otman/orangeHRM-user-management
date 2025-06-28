from time import sleep

import allure

from common_elements.side_panel import SidePanel
from pages.login_page import LoginPage

@allure.feature("Side Panel")
@allure.story("Side Panel Page")
@allure.title("Move to PIM page")
def test_side_panel(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    side_panel = SidePanel(page)
    login_page.login("Admin", "admin123")
    sleep(3)

    side_panel.move_to("PIM")
    sleep(3)
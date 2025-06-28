from time import sleep

import allure

from common_elements.side_panel import SidePanel
from pages.admin_user_management import AdminUserManagement
from pages.login_page import LoginPage
from pages.new_user_page import NewUser

@allure.feature("Add New Page")
@allure.story("Add New User")
@allure.title("Add New User with admin role and Enabled status")
def test_add_user(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    side_panel = SidePanel(page)
    login_page.login("Admin", "admin123")
    sleep(3)

    side_panel.move_to("Admin")
    sleep(3)
    admin_page = AdminUserManagement(page)
    admin_page.click_add_user_btn()
    sleep(3)
    new_user_page = NewUser(page)

    new_user_page.select_role("admin")
    new_user_page.select_status("Enabled")
    sleep(2)



@allure.feature("Add New Page")
@allure.story("Add New User")
@allure.title("Add New User with ESS role and Disabled status")
def test_add_user_ess(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    side_panel = SidePanel(page)
    login_page.login("Admin", "admin123")
    sleep(3)

    side_panel.move_to("Admin")
    sleep(3)
    admin_page = AdminUserManagement(page)
    admin_page.click_add_user_btn()
    sleep(3)
    new_user_page = NewUser(page)

    new_user_page.select_role("ESS")
    new_user_page.select_status("Disabled")
    sleep(2)
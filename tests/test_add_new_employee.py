from time import sleep

import allure
from common_elements.side_panel import SidePanel
from pages.PIM_management import PIMManagement
from pages.login_page import LoginPage
from common_elements.logout_page import LogoutPage
from pages.new_employee_page import NewEmployee

@allure.feature("Add New Employee Page")
@allure.story("Add Employee")
@allure.title("Add New employee with full name Disable status")
def test_add_new_employee_disable(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    side_panel = SidePanel(page)
    login_page.login("Admin", "admin123")
    sleep(3)

    side_panel.move_to("PIM")
    sleep(3)
    pim_page = PIMManagement(page)
    pim_page.click_add_employee_btn()
    sleep(3)

    new_employee_page = NewEmployee(page)
    new_employee_page.enter_first_name("aa")
    new_employee_page.enter_middle_name("bb")
    new_employee_page.enter_last_name("cc")
    new_employee_page.create_login_details()
    sleep(1)

    new_employee_page.enter_username("employee11")
    new_employee_page.select_disable()
    new_employee_page.enter_password("Aa123456")
    new_employee_page.enter_confirm_password("Aa123456")
    new_employee_page.click_on_save_btn()
    sleep(10)

    logout_page = LogoutPage(page)
    logout_page.logout()
    sleep(5)

    login_page.login("employee11", "Aa123456")
    sleep(3)
    assert login_page.error_message() == "Account disabled"

@allure.feature("Add New Employee Page")
@allure.story("Add Employee")
@allure.title("Add New employee with full name Enable status")
def test_add_new_employee_enable(browser_config):
    page = browser_config
    login_page = LoginPage(page)
    side_panel = SidePanel(page)
    login_page.login("Admin", "admin123")
    sleep(3)

    side_panel.move_to("PIM")
    sleep(3)
    pim_page = PIMManagement(page)
    pim_page.click_add_employee_btn()
    sleep(3)

    new_employee_page = NewEmployee(page)
    new_employee_page.enter_first_name("ali")
    new_employee_page.enter_middle_name("ali")
    new_employee_page.enter_last_name("ali")
    new_employee_page.create_login_details()
    sleep(1)

    new_employee_page.enter_username("employee22")
    new_employee_page.select_enable()
    new_employee_page.enter_password("Aa123456")
    new_employee_page.enter_confirm_password("Aa123456")
    new_employee_page.click_on_save_btn()
    sleep(10)

    logout_page = LogoutPage(page)
    logout_page.logout()
    sleep(5)

    login_page.login("employee22", "Aa123456")
    sleep(3)

    assert page.locator('.oxd-userdropdown-name').text_content() == "ali ali"
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    usernamae = page.wait_for_selector('//input[@name="username"]').type('Admin')
    password = page.wait_for_selector('//input[@name="password"]').type('admin123')
    loginBtn = page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)

    page.wait_for_selector('//a[@href="/web/index.php/admin/viewAdminModule"]').click()

######  ADD NEW USER  ######
    page.wait_for_selector('//button[text()=" Add "]').click()

    page.locator("(//div[@class='oxd-select-text-input'])[1]").click()
    page.wait_for_selector("//div[@role='option' and contains(., 'ESS')]").click()
    page.locator("(//div[@class='oxd-select-text-input'])[2]").click()
    page.wait_for_selector("//div[@role='option' and contains(., 'Enable')]").click()

    empName = page.locator("//input[@placeholder='Type for hints...']")
    empName.fill("b")
    page.locator("//div[@role='listbox']//span").first.click()
    page.wait_for_selector('(//input[@autocomplete="off"])[1]').type("John John")

    page.wait_for_selector('(//input[@type="password"])[1]').type("a1234567")
    page.wait_for_selector('(//input[@type="password"])[2]').type("a1234567")

    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(7000)


#######  SEARCH FOR USER  ######

    page.locator("//label[text()='Username']/following::input[1]").fill("john john")
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


#######  DELETE SINGLE USERS  ######
    page.wait_for_selector('(//button[@type="button"]//i[@class="oxd-icon bi-trash"])[2]').click()
    page.wait_for_timeout(3000)
    page.wait_for_selector('//button[text()=" Yes, Delete "]').click()
    page.wait_for_timeout(7000)


#######  EDIT USER  ######
    page.wait_for_selector('(//button[@type="button"]//i[@class="oxd-icon bi-pencil-fill"])[2]').click()
    page.wait_for_timeout(2000)
    page.locator('(//div[@tabindex="0"])[1]').click()
    page.wait_for_selector("//div[@role='option' and contains(., 'ESS')]").click()
    page.locator('(//div[@tabindex="0"])[2]').click()
    page.wait_for_selector("//div[@role='option' and contains(., 'Enable')]").click()

    page.wait_for_selector('//input[@placeholder="Type for hints..."]').fill('a')
    page.locator("//div[@role='listbox']//span").first.click()

    page.wait_for_selector('//input[@autocomplete="off"]').fill('asd')
    page.wait_for_timeout(2000)
    page.wait_for_selector('//input[@autocomplete="off"]').fill('qwertt')

    page.wait_for_selector('//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]').click()
    page.wait_for_selector('(//input[@type="password"])[1]').fill('1234567')
    page.wait_for_timeout(2000)
    page.wait_for_selector('(//input[@type="password"])[1]').fill('asdfghj')
    page.wait_for_timeout(2000)
    page.wait_for_selector('(//input[@type="password"])[1]').fill('12wsd')
    page.wait_for_timeout(2000)
    page.wait_for_selector('(//input[@type="password"])[1]').fill('a1234567')
    page.wait_for_timeout(2000)
    page.wait_for_selector('(//input[@type="password"])[2]').fill('b1234567')
    page.wait_for_timeout(2000)
    page.wait_for_selector('(//input[@type="password"])[2]').fill('a1234567')
    page.wait_for_timeout(5000)
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(7000)

#######  DELETE SELECTED USERS  ######
    page.locator("//div[@class='oxd-table-header']//span[contains(@class, 'oxd-checkbox-input')]").click()
    page.wait_for_timeout(2000)
    page.locator("//div[@class='oxd-table-header']//span[contains(@class, 'oxd-checkbox-input')]").click()
    page.wait_for_timeout(2000)
    page.wait_for_selector("(//div[@class='oxd-table-card']//span[contains(@class, 'oxd-checkbox-input')])[2]").click()
    page.wait_for_selector("(//div[@class='oxd-table-card']//span[contains(@class, 'oxd-checkbox-input')])[3]").click()
    page.wait_for_selector('//button[text()=" Delete Selected "]').click()
    page.wait_for_selector('//button[text()=" Yes, Delete "]').click()
    page.wait_for_timeout(7000)
    print("FINISH")


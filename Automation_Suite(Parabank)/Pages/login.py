from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        
        
        self.login_button = page.locator("input[value='Log In']")
        self.logout_link = page.locator("a[href*='logout.htm']")
        
     
        self.error_message = page.locator("#rightPanel p.error")

    def open_page(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_link.click()
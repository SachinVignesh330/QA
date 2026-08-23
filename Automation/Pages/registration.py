from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        
        
        self.first_name_input = page.locator("id=customer.firstName")
        self.last_name_input = page.locator("id=customer.lastName")
        self.street_input = page.locator("id=customer.address.street")
        self.city_input = page.locator("id=customer.address.city")
        self.state_input = page.locator("id=customer.address.state")
        self.zip_code_input = page.locator("id=customer.address.zipCode")
        self.phone_input = page.locator("id=customer.phoneNumber")
        self.ssn_input = page.locator("id=customer.ssn")
        self.username_input = page.locator("id=customer.username")
        self.password_input = page.locator("id=customer.password")
        self.confirm_password_input = page.locator("id=repeatedPassword")
        
        
        self.register_button = page.locator("input[value='Register']")
        self.welcome_title = page.locator("h1.title")
        
    def open_page(self):
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")
        
    def fill_form(self, user: dict):
        
        self.first_name_input.fill(user.get("first_name", ""))
        self.last_name_input.fill(user.get("last_name", ""))
        self.street_input.fill(user.get("address", ""))
        self.city_input.fill(user.get("city", ""))
        self.state_input.fill(user.get("state", ""))
        self.zip_code_input.fill(user.get("zip_code", ""))
        self.phone_input.fill(user.get("phone", ""))
        self.ssn_input.fill(user.get("ssn", ""))
        self.username_input.fill(user.get("username", ""))
        self.password_input.fill(user.get("password", ""))
        self.confirm_password_input.fill(user.get("confirm_password", ""))

    def click_register(self):
        self.register_button.click()
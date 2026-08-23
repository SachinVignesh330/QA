from playwright.sync_api import Page

class BillPayPage:
    def __init__(self, page: Page):
        self.page = page
        
        
        self.payee_name_input = page.locator("input[name='payee.name']")
        self.address_input = page.locator("input[name='payee.address.street']")
        self.city_input = page.locator("input[name='payee.address.city']")
        self.state_input = page.locator("input[name='payee.address.state']")
        self.zip_code_input = page.locator("input[name='payee.address.zipCode']")
        self.phone_input = page.locator("input[name='payee.phoneNumber']")
        
        self.account_input = page.locator("input[name='payee.accountNumber']")
        self.verify_account_input = page.locator("input[name='verifyAccount']")
        self.amount_input = page.locator("input[name='amount']")

        
        self.from_account_select = page.locator("select[name='fromAccountId']")
        self.send_payment_button = page.locator("input[value='Send Payment']")

       
        self.success_title = page.locator("div[id='billpayResult'] h1.title")
        self.payee_name_error = page.locator("span[id='validation-error-payee.name']")

    def open_page(self):
        self.page.goto("https://parabank.parasoft.com/parabank/billpay.htm")

    def pay_bill(self, payee_data: dict, amount: str, from_account_id: str = None):
        self.payee_name_input.fill(payee_data.get("name", payee_data.get("payee_name", "")))
        self.address_input.fill(payee_data.get("address", ""))
        self.city_input.fill(payee_data.get("city", ""))
        self.state_input.fill(payee_data.get("state", ""))
        self.zip_code_input.fill(payee_data.get("zip", payee_data.get("zip_code", "")))
        self.phone_input.fill(payee_data.get("phone", ""))
        
        account_val = payee_data.get("account", "")
        self.account_input.fill(account_val)
        self.verify_account_input.fill(payee_data.get("verify_account", account_val))
        self.amount_input.fill(amount)
        
        if from_account_id:
            self.from_account_select.select_option(from_account_id)
            
        self.send_payment_button.click()
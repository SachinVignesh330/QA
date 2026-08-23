from playwright.sync_api import Page

class RequestLoanPage:
    def __init__(self, page: Page):
        self.page = page
        
       
        self.loan_amount_input = page.locator("#amount")
        self.down_payment_input = page.locator("#downPayment")
        self.from_account_select = page.locator("#fromAccountId")
        
      
        self.apply_now_button = page.locator("input[value='Apply Now']")

    def open_page(self):
        self.page.goto("https://parabank.parasoft.com/parabank/requestloan.htm")

    def apply_for_loan(self, loan_amount: str, down_payment: str, from_account_id: str = None):
        self.loan_amount_input.fill(loan_amount)
        self.down_payment_input.fill(down_payment)
        
        if from_account_id:
            self.from_account_select.select_option(value=from_account_id)
            
        self.apply_now_button.click()
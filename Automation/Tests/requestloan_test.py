import pytest
from playwright.sync_api import expect
from Pages.registration import RegistrationPage
from Pages.request_loan import RequestLoanPage
from Config.detail_gen import get_dynamic_user_data


@pytest.fixture
def authenticated_loan_page(context):
    
    tab1 = context.new_page()
    reg_page = RegistrationPage(tab1)
    reg_page.open_page()
    
    user = get_dynamic_user_data()
    reg_page.fill_form(user)
    reg_page.click_register()
    expect(reg_page.welcome_title).to_be_visible()

    tab2 = context.new_page()
    loan_page = RequestLoanPage(tab2)
    loan_page.open_page()
    
    expect(tab2.get_by_role("heading", name="Apply for a Loan")).to_be_visible()

    return tab2


def test_TC_033(authenticated_loan_page):
    """TC_033: Request loan within available funds and get instant approval"""
    loan_page = RequestLoanPage(authenticated_loan_page)

    loan_page.apply_for_loan(loan_amount="1000", down_payment="100")

   
    expect(authenticated_loan_page.locator("#loanStatus")).to_have_text("Approved")


def test_TC_034(authenticated_loan_page):
    """TC_034: Request loan exceeding available funds gets a denial response"""
    loan_page = RequestLoanPage(authenticated_loan_page)

    loan_page.apply_for_loan(loan_amount="100000", down_payment="10")

    expect(authenticated_loan_page.locator("#loanStatus")).to_have_text("Denied")


def test_TC_035(authenticated_loan_page):
    """TC_035: Verify loan request with zero down payment"""
    loan_page = RequestLoanPage(authenticated_loan_page)

    loan_page.apply_for_loan(loan_amount="1000", down_payment="0")

   
    expect(authenticated_loan_page.get_by_role("heading", name="Loan Request Processed")).to_be_visible()
import pytest
from playwright.sync_api import expect
from Pages.registration import RegistrationPage
from Pages.billpay import BillPayPage
from Config.detail_gen import get_dynamic_user_data


@pytest.fixture
def authenticated_billpay_page(context):
  
    
    tab1 = context.new_page()
    reg_page = RegistrationPage(tab1)
    reg_page.open_page()
    
    user = get_dynamic_user_data()
    reg_page.fill_form(user)
    reg_page.click_register()
    expect(reg_page.welcome_title).to_be_visible()

    
    tab2 = context.new_page()
    bill_page = BillPayPage(tab2)
    bill_page.open_page()
    
    
    expect(tab2.get_by_role("heading", name="Bill Payment Service")).to_be_visible()

    return tab2


def get_default_payee_data():
    return {
        "payee_name": "Electric Utility Co.",
        "address": "123 Main Street",
        "city": "Beverly Hills",
        "state": "CA",
        "zip_code": "90210",
        "phone": "555-0199",
        "account": "12345",
        "verify_account": "12345"
    }


def test_TC_024(authenticated_billpay_page):
    """TC_024: Pay a payee with valid details using pay_bill()"""
    bill_page = BillPayPage(authenticated_billpay_page)
    payee_data = get_default_payee_data()

    bill_page.pay_bill(payee_data, amount="50.00")

    expect(bill_page.success_title).to_contain_text("Bill Payment Complete")

@pytest.mark.xfail(reason="Known Bug: BUG_006 - Application allows payment exceeding balance, setting balance negative")
def test_TC_026(authenticated_billpay_page):
    """TC_026: Bill Pay amount exceeds account balance"""
    bill_page = BillPayPage(authenticated_billpay_page)
    payee_data = get_default_payee_data()

    bill_page.pay_bill(payee_data, amount="500000.00")

    expect(authenticated_billpay_page.get_by_text("The amount exceeds your available balance")).to_be_visible()


@pytest.mark.xfail(reason="Known Bug: BUG_007 - Stored XSS payload causes unhandled internal server exception")
def test_TC_027(authenticated_billpay_page):
    """TC_027: Verify input sanitization against Stored XSS"""
    bill_page = BillPayPage(authenticated_billpay_page)
    payee_data = get_default_payee_data()
    payee_data["payee_name"] = "<script>alert('XSS')</script>"

    bill_page.pay_bill(payee_data, amount="50.00")

    expect(authenticated_billpay_page.locator("body")).not_to_contain_text("An internal error has occurred")
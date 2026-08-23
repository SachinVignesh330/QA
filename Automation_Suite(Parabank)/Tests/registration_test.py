import pytest
from playwright.sync_api import expect
from Pages.registration import RegistrationPage
from Config.detail_gen import get_dynamic_user_data


def test_TC_001(page):
    """TC_001: Register user with valid data"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    reg_page.fill_form(user)
    reg_page.click_register()

    expect(reg_page.welcome_title).to_be_visible()
    expect(page.get_by_text(f"Welcome {user['username']}")).to_be_visible()


def test_TC_002(page):
    """TC_002: Register with an existing/duplicate username"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    
    # First registration
    reg_page.fill_form(user)
    reg_page.click_register()

    #duplicate registration 
    reg_page.open_page()
    reg_page.fill_form(user)
    reg_page.click_register()

    expect(page.locator("span[id='customer.username.errors']")).to_have_text("This username already exists.")


@pytest.mark.xfail(reason="Known Bug: BUG_001 - Application allows duplicate personal details")
def test_TC_003(page):
    """TC_003: Register with duplicate personal details"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user1 = get_dynamic_user_data()

    
    reg_page.fill_form(user1)
    reg_page.click_register()

    
    user2 = user1.copy()
    user2["username"] = get_dynamic_user_data()["username"]

    reg_page.open_page()
    reg_page.fill_form(user2)
    reg_page.click_register()

    expect(page.get_by_text("Personal details already exist")).to_be_visible()


def test_TC_004(page):
    """TC_004: Register with empty fields"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()
    reg_page.click_register()

    expect(page.locator("span[id='customer.firstName.errors']")).to_be_visible()
    expect(page.locator("span[id='customer.lastName.errors']")).to_be_visible()
    expect(page.locator("span[id='customer.username.errors']")).to_be_visible()


def test_TC_005(page):
    """TC_005: Register with empty First Name field"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    user["first_name"] = ""

    reg_page.fill_form(user)
    reg_page.click_register()

    expect(page.locator("span[id='customer.firstName.errors']")).to_have_text("First name is required.")


def test_TC_006(page):
    """TC_006: Register with mismatched password and confirm password"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    user["password"] = "klaoa@s"
    user["confirm_password"] = "ahjio45"

    reg_page.fill_form(user)
    reg_page.click_register()

    expect(page.locator("span[id='repeatedPassword.errors']")).to_have_text("Passwords did not match.")


@pytest.mark.xfail(reason="Known Bug: BUG_002 - Application accepts non-numeric phone format")
def test_TC_007(page):
    """TC_007: Register with invalid phone number format"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    user["phone"] = "saijdcn"

    reg_page.fill_form(user)
    reg_page.click_register()

    expect(page.locator("span[id='customer.phoneNumber.errors']")).to_be_visible()


def test_TC_009(page):
    """TC_009: SQL Injection attempt in username field"""
    reg_page = RegistrationPage(page)
    reg_page.open_page()

    user = get_dynamic_user_data()
    user["username"] = "' OR '1'='1"

    reg_page.fill_form(user)
    reg_page.click_register()

    expect(page.locator("body")).not_to_contain_text("Internal Server Error")
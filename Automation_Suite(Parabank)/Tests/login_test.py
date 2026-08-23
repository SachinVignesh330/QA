import pytest
from playwright.sync_api import expect
from Pages.login import LoginPage
from Pages.registration import RegistrationPage
from Config.detail_gen import get_dynamic_user_data


@pytest.fixture
def registered_user(page):
    
    reg_page = RegistrationPage(page)
    reg_page.open_page()
    
  
    user = get_dynamic_user_data()
    
    reg_page.fill_form(user)
    reg_page.click_register()
    
    
    login_page = LoginPage(page)
    login_page.logout()
    
    return user["username"], user["password"]


def test_TC_011(page, registered_user):
    """TC_011: Login with valid credentials"""
    username, password = registered_user
    
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.login(username, password)
    
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/overview.htm")
    expect(login_page.logout_link).to_be_visible()


def test_TC_012(page, registered_user):
    """TC_012: Login with invalid password"""
    username, _ = registered_user
    
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.login(username, "WrongPassword123!")
    
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("The username and password could not be verified.")


def test_TC_013(page):
    """TC_013: Login with non-existent username"""
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.login("non_existent_user_999", "Password123!")
    
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("The username and password could not be verified.")


def test_TC_014(page):
    """TC_014: Login with empty username and password fields"""
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.login("", "")
    
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Please enter a username and password.")


def test_TC_016(page, registered_user):
    """TC_016: Verify login with leading spaces in username"""
    username, password = registered_user
    
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.login(f"   {username}", password)
    
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("The username and password could not be verified.")
import re
from playwright.sync_api import Page, expect
from pages.signup_login_page import Signup_Login

#Refactored version of the test using the Signup_Login POM:
def test_new_user_signup(page: Page) -> None:
    #Here we initialize the Page Object. NEEDS MORE COMPREHENSION
    signup_login_page = Signup_Login(page)
    #Here is where we navigate to the page
    signup_login_page.navigate()
    signup_login_page.signup_login_link.click()
    signup_login_page.username_input.fill("Kevin123")
    signup_login_page.email_input.fill("thisisdefinitlyarealemail@gmail.com")
    signup_login_page.signup_button.click()
    signup_login_page.mr_radio_button.check()
    signup_login_page.password_input.fill("fakepassword$#~ZZ")
    signup_login_page.days_dropdown.select_option("15")
    signup_login_page.months_dropdown.select_option("3")
    signup_login_page.years_dropdown.select_option("1900")
    signup_login_page.newsletter_checkbox.check()
    signup_login_page.receive_offers_checkbox.check()
    signup_login_page.first_name_input.fill("Kevin")
    signup_login_page.last_name_input.fill("Catman")
    signup_login_page.company_input.fill("thecatcompany@catmail.com")
    signup_login_page.address_input.fill("3245 Street st")
    signup_login_page.country_dropdown.select_option("United States")
    signup_login_page.state_input.fill("Ohio")
    signup_login_page.city_input.fill("Columbus")
    signup_login_page.zipcode_input.fill("43221")
    signup_login_page.mobile_number_input.fill("6987745566")
    signup_login_page.create_account_button.click()
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    try:
        page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad").click()
    except Exception:
        pass
    expect(page.get_by_text("Logged in as Kevin123")).to_be_visible()
    signup_login_page.delete_account(page)
    expect(page.get_by_text("Account Deleted!")).to_be_visible()

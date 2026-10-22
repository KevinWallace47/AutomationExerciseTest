from pages.base_page import BasePage

class Signup_Login(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_login_link = page.get_by_role("link", name=" Signup / Login")
        self.username_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup_button = page.get_by_role("button", name="Signup")
        self.password_input = page.get_by_role("textbox", name="Password *")
        self.mr_radio_button = page.get_by_role("radio", name="Mr.")
        self.mrs_radio_button = page.get_by_role("radio", name="Mrs.")
        self.days_dropdown = page.locator("#days")
        self.months_dropdown = page.locator("#months")
        self.years_dropdown = page.locator("#years")
        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.receive_offers_checkbox = page.get_by_role("checkbox", name="Receive special offers from")
        self.first_name_input = page.get_by_role("textbox", name="First name *")
        self.last_name_input = page.get_by_role("textbox", name="Last name *")
        self.company_input = page.get_by_role("textbox", name="Company", exact=True)
        self.address_input = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.country_dropdown = page.get_by_label("Country *")
        self.state_input = page.get_by_role("textbox", name="State *")
        self.city_input = page.get_by_role("textbox", name="City * Zipcode *")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.get_by_role("textbox", name="Mobile Number *")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.delete_account_link = page.get_by_role("link", name=" Delete Account")
        self.continue_link = page.get_by_role("link", name="Continue")

    def navigate(self):
        self.page.goto("https://automationexercise.com/")
    
    def delete_account(self, page):
        self.delete_account_link = page.get_by_role("link", name=" Delete Account").click()
        self.continue_link = page.get_by_role("link", name="Continue")
